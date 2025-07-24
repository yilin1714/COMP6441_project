# stage1_insecure_protocols/7_client_trust_error/server.py

"""
server.py - Client Trust Error Demonstration (Logic Flaw)

This server demonstrates a fundamental logic flaw where client-supplied data is
trusted without verification. Specifically, it accepts a 'balance' field from the client
and uses it to process sensitive operations (e.g., fund transfers) without checking
against any server-side record.

Vulnerabilities Demonstrated:
- Trusting user input for critical financial data.
- No server-side validation or cross-checking of claimed balances.
- Complete lack of access control or data integrity mechanisms.

Intended for educational purposes to illustrate the risks of blindly trusting clients
in protocol or API design.

Usage:
    python server.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

real_balance = {
    "alice": 100
}

# Vulnerability: server trusts client-supplied balance field without verification
def handle_request(data: str) -> str:
    """
    Handles incoming client requests by parsing and echoing unverified balance data.

    This function simulates a server-side logic flaw where client-supplied financial data
    (e.g., balance) is accepted and acted upon without any server-side validation.
    It demonstrates the dangers of trusting client input for critical business logic.

    Args:
        data (str): Raw key-value formatted string from the client.

    Returns:
        str: A message accepting the client action with the claimed balance, or an error message.
    """
    try:
        params = parse_kv_string(data)
        username = params.get("username")
        claimed_balance = params.get("balance")
        action = params.get("action")

        return f"✅ {username} requested '{action}' with claimed balance ${claimed_balance}. Accepted!"

    except Exception as e:
        return f"❌ Error: {e}"


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
