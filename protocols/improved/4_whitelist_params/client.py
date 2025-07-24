"""
client.py - Plaintext + Whitelisted Parameters (Improved Stage 4)

This client constructs a valid transaction request with only whitelisted fields
and sends the message in plaintext to the server. No encryption or integrity is used.

Whitelisted fields: username, action, amount

Usage:
    python client.py --port 9000
"""

import argparse

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client

# --- CLI args ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Target host")
args = parser.parse_args()

# ✅ Only include whitelisted keys
message = "username=alice&action=transfer&amount=1000"

# --- Send plaintext to server ---
response = run_tcp_client(
    host=args.host,
    port=args.port,
    plain_text=message,
    message=message,
    verbose=True
)
print()