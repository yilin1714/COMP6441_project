"""
attacker.py - Attack Demo for AES Without Integrity or Authentication

This script simulates several invalid client requests to test how a server that
uses AES encryption (without MAC or authentication) responds to malformed input.

Attack Scenarios:
1. Sending plaintext instead of ciphertext
2. Sending random hex-encoded garbage
3. Sending empty or invalid hex

Usage:
    python attacker.py --port 9000
"""

import argparse
import random
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port to attack")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Attack 1: Send raw plaintext
plaintext_1 = "username=attacker&action=drain&amount=999999"
payload_1 = plaintext_1  # not encrypted at all

# Attack 2: Send random hex garbage
random_bytes = bytes(random.choices(range(256), k=32))
plaintext_2 = "[random hex garbage]"
payload_2 = random_bytes.hex()

# Attack 3: Send invalid/empty hex string
plaintext_3 = "[empty message]"
payload_3 = "zzzz"  # invalid hex

# Execute all attacks
run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plaintext_1,
    payload=payload_1,
    verbose=True
)
time.sleep(0.6)

run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plaintext_2,
    payload=payload_2,
    verbose=True
)
time.sleep(0.6)

run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plaintext_3,
    payload=payload_3,
    verbose=True
)

print()