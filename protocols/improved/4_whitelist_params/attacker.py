"""
attacker.py - Whitelist Bypass Attempt (Stage 4 - Plaintext Mode)

This script simulates an attacker trying to inject forbidden parameters
into a request. The server should reject any parameter not in the approved whitelist.

In this version, no encryption or MAC is used — messages are sent in plaintext.

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

# --- Parse CLI arguments ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

# ❌ Inject a forbidden parameter 'is_admin=true'
injected_message = "username=admin&action=override&amount=999999&is_admin=true"

# Send the forged plaintext message
run_tcp_attack(
    host=args.host,
    port=args.port,
    plain_text=injected_message,
    payload=injected_message,
    verbose=True
)

print()