"""
attacker.py - Attack Demo for Plaintext + HMAC Protocol

This script simulates tampering attempts on a plaintext protocol that uses HMAC-SHA256
for integrity protection. It demonstrates how the server rejects messages with:

1. Missing MAC
2. Invalid (forged) MAC
3. Valid MAC but tampered message

Usage:
    python attacker.py --port 9000
"""

import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack
from utils.mac_utils import compute_mac

# --- Argument parsing ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to attack")
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

host = args.host
port = args.port

# --- Attack 1: Missing MAC field ---
payload1 = "username=intruder&action=withdraw&amount=5000"
run_tcp_attack(
    host=host,
    port=port,
    plain_text=payload1,
    payload=payload1,
    verbose=True
)
time.sleep(0.5)

# --- Attack 2: Invalid (forged) MAC ---
payload2 = "username=intruder&action=withdraw&amount=5000&mac=deadbeef"
run_tcp_attack(
    host=host,
    port=port,
    plain_text=payload2,
    payload=payload2,
    verbose=True
)
time.sleep(0.5)

# --- Attack 3: Valid MAC but message tampered ---
# First build a legitimate message
original = "username=alice&action=transfer&amount=1000"
valid_mac = compute_mac(original)
# Now modify the message content but keep old MAC
tampered = "username=alice&action=transfer&amount=9000&mac=" + valid_mac
run_tcp_attack(
    host=host,
    port=port,
    plain_text=tampered,
    payload=tampered,
    verbose=True
)

print()