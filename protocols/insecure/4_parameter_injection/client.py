# stage1_insecure_protocols/4_parameter_injection/client.py

"""
client.py - Insecure Protocol Demo (Parameter Injection - Benign Client)

This client sends a plaintext key-value request without encryption or integrity protection.
It illustrates how insecure clients interact with vulnerable servers in the absence of
authentication, allowing for parameter injection if misused.

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

# Create a standard transaction message to simulate normal client behavior
plain_text = "username=alice&action=transfer&amount=1000"
message = plain_text

# Send the plaintext transaction message to the vulnerable server
response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)

print()
