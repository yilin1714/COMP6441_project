# stage1_insecure_protocols/8_predictable_token/client.py

"""
client.py - Predictable Session ID Demo (Honest Client)

This script represents a benign client that sends a request using a known, valid
session ID to a server that authenticates users solely based on session tokens.

While the session_id is legitimate, the demonstration exposes the insecurity of using
static and predictable session tokens without expiration, validation, or user context.

This scenario emphasizes how even honest clients can participate in flawed protocols
that may be vulnerable to token prediction or replay attacks.

Usage:
    python client.py --port 9000
"""

import argparse
from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Construct a legitimate-looking request using a known, predictable session ID
plain_text = "session_id=123456&action=transfer&amount=500"
message = plain_text

# Send the request to the server to demonstrate the insecure acceptance of static tokens
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)

print()