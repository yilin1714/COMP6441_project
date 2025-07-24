"""
attacker.py - Session ID Attack Demo (Stage 5 - Plaintext Protocol)

This script simulates a malicious client attempting to bypass session
verification by:
- Omitting the session_id entirely
- Forging a fake session_id

The server should reject both requests if session tracking is enforced correctly.

Usage:
    python attacker.py --port 9000
"""

import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

# Attack 1: Missing session_id
def attack_missing_session(host, port):
    print("\n[Attack 1] Sending request WITHOUT session_id...")
    plain = "username=admin&action=steal&amount=999999"
    run_tcp_attack(host, port, plain, plain, verbose=True)

# Attack 2: Fake session_id
def attack_fake_session(host, port):
    print("\n[Attack 2] Sending request with FAKE session_id...")
    plain = "session_id=notarealsession123&username=hacker&action=withdraw&amount=888888"
    run_tcp_attack(host, port, plain, plain, verbose=True)

# Main execution
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

attack_missing_session(args.host, args.port)
time.sleep(0.8)
attack_fake_session(args.host, args.port)

print()