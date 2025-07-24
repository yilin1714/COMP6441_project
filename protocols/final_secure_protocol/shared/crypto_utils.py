# shared/crypto_utils.py

import hmac
import hashlib
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def generate_iv() -> bytes:
    """
    Generate a secure 16-byte IV for AES-CBC.
    """
    return secrets.token_bytes(16)


def aes_encrypt(plaintext: str, key: bytes) -> str:
    """
    Encrypt plaintext using AES-CBC with PKCS7 padding.

    Returns:
        str: Hex-encoded IV + ciphertext.
    """
    iv = generate_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return (iv + ciphertext).hex()


def aes_decrypt(cipher_hex: str, key: bytes) -> str:
    """
    Decrypt AES-CBC hex string.

    Returns:
        str: Decrypted plaintext.
    """
    raw = bytes.fromhex(cipher_hex)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()


def hmac_sign(message: str, key: bytes) -> str:
    return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()


def hmac_verify(message: str, signature: str, key: bytes) -> bool:
    """
    Verify HMAC-SHA256 signature.

    Returns:
        bool: True if valid, False otherwise.
    """
    expected = hmac.new(key, message.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, expected)


def current_timestamp() -> int:
    """
    Get the current UNIX timestamp in seconds.

    Returns:
        int: Current time.
    """
    import time

    return int(time.time())
