"""
attacker.py - Stage 8: Token Forgery & Missing Token Simulation

Simulates two attacks:
1. Sending a request with no token
2. Sending a request with a forged/fake token

Usage:
    python attacker.py --port 9000
"""

import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack


def attack_missing_token(host, port):
    print("\n[Attack 1] Sending request WITHOUT token...")
    payload = "username=intruder&action=transfer&amount=999999"
    run_tcp_attack(
        host=host,
        port=port,
        plain_text=payload,
        payload=payload,
        verbose=True
    )


def attack_forged_token(host, port):
    print("\n[Attack 2] Sending request WITH FAKE token...")
    fake_token = "hacker.9999999999.fakehmacsignature"
    payload = f"token={fake_token}&action=steal&amount=1000000"
    run_tcp_attack(
        host=host,
        port=port,
        plain_text=payload,
        payload=payload,
        verbose=True
    )


# --- CLI argument parsing ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

# --- Run attacks ---
attack_missing_token(args.host, args.port)
time.sleep(1)
attack_forged_token(args.host, args.port)
print()