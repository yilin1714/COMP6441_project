# stage1_insecure_protocols/4_parameter_injection/server.py

"""
server.py - Insecure Protocol Demo (Parameter Injection)

This server accepts plaintext requests formatted as key=value pairs joined by '&'.
It demonstrates the risk of parameter injection when the server blindly parses
unvalidated input into command parameters without authentication or integrity checks.

Vulnerabilities demonstrated:
- No input validation: arbitrary keys can be injected (e.g., "admin=true&...")
- No authentication: any user can issue sensitive commands.
- No integrity: malformed or tampered requests are blindly accepted.

Educational purpose: illustrates how parsing untrusted input without checks
can lead to unintended behavior or logic flaws.
"""

import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(raw_data: str) -> str:
    """
    Processes an incoming plaintext request string and returns a confirmation response.

    This function parses a raw key-value string (e.g., "username=bob&action=transfer&amount=100")
    without any form of validation, authentication, or integrity checking. It is used to
    demonstrate how parameter injection vulnerabilities arise when untrusted input is blindly parsed.

    Args:
        raw_data (str): Raw request message from the client.

    Returns:
        str: A confirmation message if parsing succeeds, or an error message otherwise.
    """
    try:
        params = parse_kv_string(raw_data)
        user = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        response = f"✅ Action '{action}' by '{user}' for ${amount} accepted."
        return response

    except Exception as e:
        error_msg = f"❌ Error parsing request: {e}"
        return error_msg


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional port to notify when ready")
args = parser.parse_args()

# Launch vulnerable server that blindly parses unvalidated input
run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
