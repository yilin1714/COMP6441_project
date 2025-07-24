# stage1_insecure_protocols/8_predictable_token/server.py

"""
server.py - Predictable Token Authentication Demo

This server simulates a vulnerable authentication scheme where users are
authenticated solely based on predictable session IDs. It uses a static
mapping of session IDs to usernames and accepts actions based on a client-supplied
session_id field.

Vulnerabilities Demonstrated:
- Use of easily guessable session tokens.
- No expiration, binding, or cryptographic verification.
- Complete trust in client-provided session IDs.

Educational Purpose:
To illustrate the risks of insecure session management practices and emphasize
the importance of strong, unpredictable authentication tokens in protocol design.

Usage:
    python server.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

# Simulated session token mapping (predictable IDs)
session_db = {
    "123456": "alice",
    "123457": "bob"
}

def handle_request(data: str) -> str:
    """
    Processes an incoming request using a predictable session ID.

    This function parses key-value string data received from the client,
    extracts a session_id and associated action parameters, and attempts
    to match the session_id against a static session database.

    This design intentionally demonstrates a vulnerability where predictable
    session IDs are used as the sole authentication mechanism.

    Args:
        data (str): Raw client request string, expected in the format
                    "session_id=...&action=...&amount=..."

    Returns:
        str: A success message if the session_id is valid, otherwise an error response.
    """
    try:
        params = parse_kv_string(data)
        sid = params.get("session_id")
        action = params.get("action")
        amount = params.get("amount")

        user = session_db.get(sid)

        if user:
            return f"✅ Session '{sid}' recognized as '{user}'. {action} of ${amount} approved."
        else:
            return "❌ Invalid or unknown session_id."
    except Exception as e:
        return f"❌ Error processing request: {e}"

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port")
args = parser.parse_args()

 # Launch a server that uses predictable session IDs for authentication (vulnerable design)
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)