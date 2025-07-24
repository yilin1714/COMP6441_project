# stage1_insecure_protocols/5_fixed_session_id/server.py

"""
server.py - Fixed Session ID Authentication Demo

This server simulates an insecure session management model where access is granted
solely based on a fixed session ID, without any validation of expiration time,
device association, IP binding, or reauthentication.

Vulnerabilities Demonstrated:
- Session IDs are static and predictable.
- No expiration or revocation logic.
- Full trust is placed in the client-provided session_id parameter.

Intended for educational use in demonstrating the dangers of improper session handling
in protocol design.

Usage:
    python server.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

# Predefined session database
session_store = {
    "abc123": "alice",
    "xyz789": "bob"
}


def handle_request(data: str) -> str:
    """
    Handles incoming requests by checking a fixed session ID.

    This function parses a key-value string from the client and attempts to extract a session_id.
    It performs a lookup in the static session_store without validating session expiration,
    device binding, or reauthentication. If the session ID is recognized, it accepts the requested
    action; otherwise, it rejects the request.

    Args:
        data (str): The raw request string in the format "session_id=...&action=...&amount=..."

    Returns:
        str: A response indicating whether the session ID was accepted and the action was authorized.
    """
    try:
        params = parse_kv_string(data)
        sid = params.get("session_id", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        username = session_store.get(sid, None)

        if username:
            response = f"✅ Session '{sid}' identified as '{username}': action '{action}' of ${amount} accepted."
            return response

        else:
            response = f"❌ Invalid session_id."
            return response

    except Exception as e:
        error_msg = f"❌ Request error: {e}"
        return error_msg


# Launch server that accepts actions based on fixed session IDs (no expiry or validation)
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
