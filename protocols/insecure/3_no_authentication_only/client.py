import argparse

from config import DEFAULT_HOST

from utils.aes_utils import encrypt
from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number of the server")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=alice&action=transfer&amount=1000"

ciphertext_hex = encrypt(plain_text, return_hex=True)

response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=ciphertext_hex,
    verbose=True
)

print()
