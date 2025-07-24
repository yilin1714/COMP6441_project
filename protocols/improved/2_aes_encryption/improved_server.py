"""
improved_server.py - AES Encryption Demo (Modularized)

This server demonstrates AES-based message decryption using a shared key.
It replaces Base64-only encoding from earlier stages with real AES encryption,
and leverages a centralized aes_utils module for all crypto operations.

Vulnerabilities:
- ❌ No integrity check (MAC/HMAC missing)
- ❌ No authentication: server accepts any valid-looking message

Usage:
    python improved_server.py --port 9000 [--notify-port 9100]
"""

import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server
from utils.aes_utils import decrypt  # ✅ use central AES utility

def handle_request(data: str) -> str:
    """
    Decrypts and processes an AES-encrypted Base64-encoded request string.

    Args:
        data (str): Base64-encoded AES-ECB encrypted message string.

    Returns:
        str: Confirmation response or decryption failure message.
    """
    plaintext = decrypt(data)
    if plaintext.startswith("[!]"):
        return plaintext

    params = parse_kv_string(plaintext)
    username = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Decrypted. Action '{action}' by '{username}' with amount ${amount} accepted."


# --- Startup CLI ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Notify port for demo UI")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)