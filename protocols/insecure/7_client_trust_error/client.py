# stage1_insecure_protocols/7_client_trust_error/client.py

"""
client.py - Client Trust Error Demo (Benign Client)

This script simulates a client that sends a transaction request containing a balance
field to a vulnerable server. The server is expected to blindly trust the balance
without validating it against any authoritative source.

Purpose:
- Demonstrate how even benign clients can exploit or unintentionally benefit from
  insecure server logic that trusts client-supplied financial values.

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

# Construct a transaction request that includes a client-supplied balance
plain_text = "username=alice&balance=100&action=withdraw"
message = plain_text

# Send the transaction request to a server that does not validate balance
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)

print()