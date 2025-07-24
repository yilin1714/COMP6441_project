"""
client.py - Plaintext + HMAC Client (Improved Stage 3)

This client prepares a transaction message, appends an HMAC-SHA256 for integrity,
and sends the full message in plaintext to the server.

Security Properties:
- ✅ HMAC-SHA256 provides message integrity
- ❌ No encryption: message contents are visible in transit
- ❌ No authentication or replay protection

Usage:
    python client.py --port 9000
"""

import argparse

from config import DEFAULT_HOST
from utils.mac_utils import compute_mac
from utils.client_runner import run_tcp_client

# --- CLI argument parsing ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Server host")
args = parser.parse_args()

# --- Construct plaintext message ---
message = "username=alice&action=transfer&amount=1000"
mac = compute_mac(message)
full_message = f"{message}&mac={mac}"

# --- Send plaintext + MAC to server ---
response = run_tcp_client(
    host=args.host,
    port=args.port,
    plain_text=message,
    message=full_message,
    verbose=True
)
print()
