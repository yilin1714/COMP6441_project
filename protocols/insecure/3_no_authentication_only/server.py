# stage1_insecure_protocols/3_no_authentication_only/server.py

"""
server.py - Insecure Protocol Demo (AES Encryption, No Authentication)

This server accepts AES-encrypted messages from the client, decrypts them using
a shared symmetric key, and processes the resulting plaintext request. However,
no authentication is performed, meaning any party with access to the key can
forge valid requests.

Vulnerabilities demonstrated:
- No identity verification: the server assumes the decrypted content is trustworthy.
- Shared-key misuse: attackers with the key can impersonate users or modify requests.
- No message integrity: tampered ciphertext is not authenticated.

This module demonstrates why encryption alone is insufficient without authentication.
"""

import argparse

from config import DEFAULT_HOST

from utils.aes_utils import decrypt
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(ciphertext_hex: str) -> str:
    """
    Handles an incoming AES-encrypted message, decrypts it, and returns a response.

    This function demonstrates the insecurity of using encryption without authentication.
    It decrypts the provided ciphertext using a shared symmetric AES key, parses the
    resulting plaintext message assuming a key-value format, and generates a response
    confirming the requested action. The decrypted content is blindly trusted.

    Args:
        ciphertext_hex (str): AES-encrypted payload in hex-encoded string form.

    Returns:
        str: Server's response echoing the request contents, or an error message if decryption fails.
    """
    decrypted = decrypt(ciphertext_hex)
    if decrypted.startswith("[!]"):
        return f"❌ Error: {decrypted}"

    print(f"   Decrypted message: {decrypted}")
    params = parse_kv_string(decrypted)

    user = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Action '{action}' by '{user}' for ${amount} accepted."



parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server on")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

# Launch the AES-only server (no authentication, insecure by design)
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
