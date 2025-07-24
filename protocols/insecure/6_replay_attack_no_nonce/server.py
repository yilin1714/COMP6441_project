"""
server.py - Insecure Protocol Demo (No Authentication, No Encryption)

This script implements a TCP server that processes plaintext client messages without
any form of authentication, encryption, or integrity validation.

Vulnerabilities demonstrated:
- Plaintext transmission: messages are sent unencrypted and can be intercepted or modified.
- No authentication: server accepts commands from any client.
- No integrity checks: malformed or tampered requests are processed without verification.

The server is for educational use only and is designed to highlight protocol design flaws
that may lead to serious security vulnerabilities in real-world systems.

Usage:
    python server.py --port 9000 [--notify-port 9100]
"""

import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(data):
    """
    Handles incoming transaction request messages sent in plaintext.

    This function parses a URL-style key-value string representing a transaction command
    and generates a confirmation response. It assumes the data is untrusted and does
    not perform any authentication or validation.

    Args:
        data (str): Raw request string in the format "username=...&action=...&amount=..."

    Returns:
        str: A response string confirming the action, username, and amount.
    """
    params = parse_kv_string(data)
    username = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Action '{action}' by '{username}' with amount ${amount} accepted."


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number the server will bind to")
parser.add_argument("--notify-port", type=int, required=False,
                    help="Optional notify port to report READY status to run_demo")
args = parser.parse_args()

# Launch the insecure server with a basic transaction handler
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)