# protocols/improved/1_no_auth_no_encryption/client.py

"""
client.py - Improved Protocol Demo (Adds Password Authentication)

This client connects to the improved version of the Stage 1 server,
sending a plaintext transaction request that includes a password
for basic authentication.

Security Improvements Demonstrated:
- ✅ Requires a password to authenticate the client.
- ⚠️ Still transmits data in plaintext, so credentials can be intercepted.
- ❌ No encryption or integrity checks (covered in later stages).

This version is intended to demonstrate a minimal improvement over
a fully insecure design by introducing a simple shared-secret mechanism.

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

plain_text = "username=alice&action=transfer&amount=1000&password=cybersecurity"
message = plain_text

# Send message with password-based authentication (but still no encryption)
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)
print()
