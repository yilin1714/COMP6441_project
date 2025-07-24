# protocols/improved/1_add_password_auth/improved_server.py

"""
improved_server.py - Improved Protocol Demo (Adds Basic Password Authentication)

This script demonstrates a slightly improved version of the insecure protocol
by requiring a static password for any incoming transaction request. Messages
remain in plaintext and are unauthenticated otherwise.

Improvements:
- ✅ Basic password-based authentication to prevent unauthenticated commands.
- ⚠️ Still no encryption: messages can be intercepted and read in transit.
- ⚠️ No integrity check: message tampering is not detected.

This server is for educational use only and highlights how small changes can
improve protocol security, while also revealing remaining weaknesses.

Usage:
    python improved_server.py --port 9000 [--notify-port 9100]
"""

import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

# Shared server-side password (for demo only — do NOT hardcode in real apps)
SERVER_PASSWORD = "cybersecurity"


def handle_request(data):
    """
    Handles incoming transaction requests with basic authentication.

    Args:
        data (str): Raw request string in the format
                    "username=...&action=...&amount=...&password=..."

    Returns:
        str: Response indicating success or authentication failure.
    """
    params = parse_kv_string(data)

    if params.get("password") != SERVER_PASSWORD:
        return "[!] Authentication failed: invalid or missing password."

    username = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Authenticated. Action '{action}' by '{username}' with amount ${amount} accepted."


# Parse CLI arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number the server will bind to")
parser.add_argument("--notify-port", type=int, required=False,
                    help="Optional notify port to report READY status to run_demo")
args = parser.parse_args()

# Start the server
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
