# stage1_insecure_protocols/2_base64_fake_encryption/client.py

"""
client.py - Base64 Fake Encryption Demo

This client sends a Base64-encoded message to the server.
It demonstrates how a protocol may falsely assume security
by using reversible encoding rather than actual encryption.

Vulnerabilities:
- Base64 is not encryption and offers no confidentiality.
- The server does not authenticate clients or verify message integrity.

Usage:
    python client.py --port 9000
"""

import base64
import argparse

from config import DEFAULT_HOST

from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Prepare a simple transaction message to be sent insecurely
plain_text = "username=alice&action=transfer&amount=1000"

encoded = base64.b64encode(plain_text.encode()).decode()

# Send the Base64-encoded message to the server; plaintext shown for reference
response = run_tcp_client(server_host, server_port, plain_text, encoded, verbose=True)

print()