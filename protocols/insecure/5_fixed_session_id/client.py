# stage1_insecure_protocols/5_fixed_session_id/client.py

"""
client.py - Insecure Protocol Demo (Fixed Session ID)

This client sends a request containing a known session_id to simulate
a vulnerable session-based authentication system that lacks expiry or binding.

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

# Simulate a legitimate user sending a valid transaction with a static session ID
plain_text = "session_id=abc123&action=transfer&amount=1000"
message = plain_text

# Send the session-based request to the insecure server
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)

print()
