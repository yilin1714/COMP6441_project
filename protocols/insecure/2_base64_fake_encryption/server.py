# stage1_insecure_protocols/2_base64_fake_encryption/server.py

"""
server.py - Insecure Protocol Demo (Base64 Fake Encryption)

This script implements a basic TCP server that receives Base64-encoded messages from clients,
decodes them, and responds as if they were securely transmitted. It simulates an insecure protocol
commonly found in misconfigured systems where encoding is mistaken for encryption.

Key vulnerabilities demonstrated:
- Base64 encoding is not encryption and offers no confidentiality.
- No authentication is performed: any client can impersonate a user.
- No message integrity checks: the server does not validate the authenticity or structure of requests.
- Sensitive operations (e.g., fund transfers) are processed without validation or protection.

This server is designed for educational or demonstration environments to highlight the dangers
of substituting encoding for encryption and omitting essential security protocols.
"""

import base64
import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

def handle_request(encoded_data):
    """
    Handles an incoming Base64-encoded request message from the client.

    This function simulates a flawed server that treats Base64 encoding as if it
    provides encryption. It decodes the message, parses it as a URL-style key-value
    string, and constructs a confirmation response. No authentication or validation
    is performed.

    Args:
        encoded_data (str): A Base64-encoded string in the format
                            "username=...&action=...&amount=..."

    Returns:
        str: A formatted success response if decoding and parsing succeed,
             or an error message if any exception occurs.
    """

    try:
        decoded = base64.b64decode(encoded_data).decode()
        print(f"   Decoded message: {decoded}")

        params = parse_kv_string(decoded)
        username = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        response = f"✅ Action '{action}' by '{username}' with amount ${amount} accepted."
        return response

    except Exception as e:
        error_msg = f"❌ Error: Failed to decode or parse message. ({e})"
        return error_msg

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number the server will bind to")
parser.add_argument("--notify-port", type=int, required=False,
                    help="Optional notify port to report READY status to run_demo")
args = parser.parse_args()

# Launch the insecure Base64 server with a fake encryption handler
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)