"""
improved_server.py - Session-Based Protocol (Plaintext + Session ID, Stage 5)

This server introduces stateful session validation. A client must first initiate a session
by sending a request with `action=init`. The server replies with a unique session_id.

All future requests must include the valid session_id in plaintext, or they will be rejected.

Improvements:
- ✅ Server-managed session IDs (UUIDv4)
- ✅ Enforces per-request session validation
- ❌ No encryption: requests are readable in transit
- ❌ No integrity check or user authentication

Usage:
    python improved_server.py --port 9000 [--notify-port 9100]
"""

import argparse
import uuid

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

# Active session store (in-memory)
active_sessions = set()

def generate_session_id() -> str:
    """Generates a secure random session ID and registers it."""
    sid = uuid.uuid4().hex
    active_sessions.add(sid)
    return sid

def handle_request(data: str) -> str:
    """
    Processes plaintext requests and enforces session ID validation.

    Special command: if action=init, server returns a new session ID.
    Otherwise, session_id must be present and valid.
    """
    try:
        params = parse_kv_string(data)

        if params.get("action") == "init":
            sid = generate_session_id()
            return f"🎯 Your session_id: {sid}"

        session_id = params.get("session_id")
        if session_id not in active_sessions:
            return "[!] Invalid or missing session_id."

        username = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Session verified. Action '{action}' by '{username}' with amount ${amount} accepted."

    except Exception as e:
        return f"[!] Error processing request: {e}"


# --- CLI Argument Handling ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)