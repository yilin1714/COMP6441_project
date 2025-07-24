import argparse

from config import DEFAULT_HOST
from utils.aes_utils import encrypt
from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Server host (default: 127.0.0.1)")
args = parser.parse_args()

plaintext = "username=alice&action=transfer&amount=1000"
ciphertext = encrypt(plaintext, return_hex=True)

response = run_tcp_client(
    host=args.host,
    port=args.port,
    plain_text=plaintext,
    message=ciphertext,
    verbose=True
)
print()
