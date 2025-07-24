"""
improved_server.py - Whitelist Parameters Only (Improved Stage 4)

This server receives messages in plaintext and validates that only allowed parameters are included.
It demonstrates protection against parameter injection without encryption or integrity mechanisms.

Improvements:
- ✅ Enforces a strict whitelist of accepted fields
- ❌ No encryption: messages are readable in transit
- ❌ No integrity or tamper detection
- ❌ No user authentication or replay protection

Usage:
    python improved_server.py --port 9000 [--notify-port 9100]
"""

import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

# Whitelisted keys that are allowed in the request
WHITELIST_KEYS = {"username", "action", "amount"}

def handle_request(data: str) -> str:
    """
    Parses plaintext request, enforces whitelist of parameters.

    Args:
        data (str): Plaintext message in key=value&... format

    Returns:
        str: Success response or error message if parameters are invalid
    """
    try:
        params = parse_kv_string(data)

        # Enforce whitelist of keys
        for key in params:
            if key not in WHITELIST_KEYS:
                return f"[!] Unexpected parameter '{key}' is not allowed."

        username = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Validated. Action '{action}' by '{username}' with amount ${amount} accepted."

    except Exception as e:
        return f"[!] Error processing request: {e}"


# --- CLI Startup ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)