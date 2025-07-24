"""
improved_server.py - Protocol Demo (Plaintext + HMAC Integrity)

This server accepts plaintext requests with an attached HMAC-SHA256.
It verifies the MAC to ensure the message has not been tampered with.

Improvements:
- ✅ HMAC-SHA256 verifies integrity of message content
- ✅ Prevents undetected modification even over plaintext
- ❌ No encryption: attackers can read the message
- ❌ No authentication or replay prevention

Usage:
    python improved_server.py --port 9000 [--notify-port 9100]
"""

import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server
from utils.mac_utils import verify_mac

def handle_request(data: str) -> str:
    """
    Processes a plaintext request containing a trailing HMAC.

    Args:
        data (str): The full message in format "key1=...&key2=...&...&mac=..."

    Returns:
        str: Confirmation or error message based on MAC validation.
    """
    ok, result = verify_mac(data)
    if not ok:
        return result  # result is an error message like [!] MAC missing or failed

    params = parse_kv_string(result)
    username = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Verified. Action '{action}' by '{username}' with amount ${amount} accepted."


# --- CLI Setup ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)