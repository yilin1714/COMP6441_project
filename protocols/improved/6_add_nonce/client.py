"""
client.py - Replay Attack Demo with Nonce (Plaintext)

Sends a plaintext transfer request with a nonce.
Server will reject reused nonces to prevent replay attacks.

Usage:
    python client.py --port 9000 [--nonce abc123]
"""

import argparse
import random
import string

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client


def generate_nonce(length=16):
    """Generate a random alphanumeric nonce."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# --- CLI Argument Parsing ---

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
parser.add_argument("--nonce", type=str, help="Optional fixed nonce for replay testing")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

# --- Compose Plaintext Request ---

nonce = args.nonce if args.nonce else generate_nonce()
plain_text = f"username=alice&action=transfer&amount=1000&nonce={nonce}"

# --- Send Plaintext Request (no encryption) ---

response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=plain_text,  # no encoding, pure string
    verbose=True
)

print()