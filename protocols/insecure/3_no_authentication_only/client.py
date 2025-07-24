# stage1_insecure_protocols/3_no_authentication_only/client.py

"""
client.py - Encrypted But No Authentication

This client encrypts a sensitive request using AES and sends it to the server.
Although the message is encrypted, there is no authentication or identity verification.

Vulnerabilities:
- No authentication mechanism (e.g., token, HMAC, signature)
- Any party with the shared key can send forged messages
- The server blindly trusts decrypted content without validation

Usage:
    python client.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.aes_utils import encrypt
from utils.client_runner import run_tcp_client

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number of the server")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# Prepare a sensitive financial transaction request
plain_text = "username=alice&action=transfer&amount=1000"

# Encrypt the message using AES (note: encryption alone does not guarantee authenticity)
ciphertext_hex = encrypt(plain_text, return_hex=True)

# Send AES-encrypted message (hex-encoded) to the server without authentication
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=ciphertext_hex,
    verbose=True
)

print()
