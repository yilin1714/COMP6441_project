# shared/auth_utils.py

import hashlib
import hmac
import json
import secrets
import time

from config import AES_KEY
from utils.parser_utils import parse_kv_string
from .config import USER_DB, PASSWORD_SALT, HMAC_KEY, TOKEN_EXPIRY_SECONDS, NONCE_CACHE, NONCE_CACHE_MAX
from .crypto_utils import aes_encrypt, aes_decrypt


def verify_user(username: str, password_hash: str) -> bool:
    """
    Verify the given password hash against stored user data.

    Returns True if valid user and password match.
    """
    stored_hash = USER_DB.get(username)
    return stored_hash == password_hash


def generate_token(username: str) -> str:
    """
    Generate a signed session token for a user with expiry timestamp.

    Token format: base64-encoded JSON + HMAC signature
    """
    payload = {
        "username": username,
        "exp": int(time.time()) + TOKEN_EXPIRY_SECONDS
    }

    payload_str = "&".join(f"{k}={v}" for k, v in payload.items())
    signature = hmac.new(HMAC_KEY, payload_str.encode(), hashlib.sha256).hexdigest()

    token_plain = f"{payload_str}&sig={signature}"

    return aes_encrypt(token_plain, AES_KEY)


def verify_token(token_str: str) -> str | None:
    """
    Verify token's HMAC signature and expiration time.

    Returns username if valid; otherwise None.
    """
    try:
        # Step 1: AES decrypt token string
        decrypted = aes_decrypt(token_str, AES_KEY)

        # Step 2: Parse decrypted query string
        params = parse_kv_string(decrypted)

        payload_fields = {k: v for k, v in params.items() if k != "sig"}
        payload_str = "&".join(f"{k}={v}" for k, v in payload_fields.items())
        received_sig = params.get("sig")

        if not received_sig:
            return None

        # Step 3: Verify signature
        expected_sig = hmac.new(HMAC_KEY, payload_str.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(received_sig, expected_sig):
            return None

        # Step 4: Check expiry
        if "exp" not in params or time.time() > int(params["exp"]):
            return None

        return params.get("username")

    except Exception:
        return None


def generate_nonce() -> str:
    """
    Generate a cryptographically secure random nonce.
    """
    return secrets.token_hex(16)


def is_replay_nonce(username: str, nonce: str) -> bool:
    return nonce in NONCE_CACHE[username]


def save_nonce(username: str, nonce: str):
    user_set = NONCE_CACHE[username]
    user_set.add(nonce)
    if len(user_set) > NONCE_CACHE_MAX:
        user_set.pop()


def hash_password(password: str, salt: str = PASSWORD_SALT) -> str:
    """
    Hash the given password with a salt using SHA-256.

    Returns:
        str: Hex-encoded hash.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()
