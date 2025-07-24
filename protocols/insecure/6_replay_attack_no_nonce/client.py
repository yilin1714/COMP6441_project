"""
client.py - Replay Attack Demo (Plaintext, No Nonce)

Sends a plaintext transaction request to the server without any replay protection.
This simulates a normal user initiating a sensitive action in an insecure protocol.

Usage:
    python client.py --port 9000
"""

import argparse

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client

# --- Parse CLI arguments ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# --- Construct a plaintext transaction request ---
plain_text = "username=alice&action=transfer&amount=1000"

# --- Send the request as string (no encoding) ---
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=plain_text,  # send as str to match server
    verbose=True
)

print()