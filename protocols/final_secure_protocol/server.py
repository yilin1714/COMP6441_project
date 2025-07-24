import argparse
import json

from config import DEFAULT_HOST
from shared.crypto_utils import aes_decrypt, hmac_verify
from shared.auth_utils import (
    verify_user,
    verify_token,
    is_replay_nonce,
    save_nonce,
    generate_token,
)
from shared.config import AES_KEY, HMAC_KEY
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(encrypted_data: str) -> str:
    try:
        decrypted = aes_decrypt(encrypted_data, AES_KEY)
        params = parse_kv_string(decrypted)

        if params.get("action") == "login":
            username = params.get("username")
            password_hash = params.get("password")
            nonce = params.get("nonce")

            if not username or not password_hash or not nonce:
                return "❌ Missing fields in login request."

            if is_replay_nonce(username, nonce):
                return "❌ Replay attack detected.."

            if not verify_user(username, password_hash):
                return "❌ Invalid username or password."

            save_nonce(username, nonce)

            token = generate_token(username)
            return token

        elif params.get("action") == "transfer":
            payload_str, received_mac = decrypted.rsplit("&", 1)

            if not received_mac:
                return "❌ Malformed transaction request."

            received_mac = parse_kv_string(received_mac)

            if not hmac_verify(payload_str, received_mac.get("mac"), HMAC_KEY):
                return "❌ HMAC integrity check failed!"

            data = parse_kv_string(payload_str)

            token = data.get("token")
            action = data.get("action")
            amount = data.get("amount")
            nonce = data.get("nonce")

            if not token or not action or not amount or not nonce:
                return "❌ Missing fields in transaction payload."

            username = verify_token(token)
            if not username:
                return "❌ Invalid or expired session token."

            if is_replay_nonce(username, nonce):
                return "❌ Replay attack detected."

            save_nonce(username, nonce)
            return f"✅ Success! {username} performed {action} of ${amount}."

        else:
            return "❌ Unknown request format."

    except Exception as e:
        return f"❌ Server error: {str(e)}"


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number the server will bind to")
parser.add_argument("--notify-port", type=int, required=False,
                    help="Optional notify port to report READY status to run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    host=DEFAULT_HOST,
    handle_request=handle_request,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None,
)
