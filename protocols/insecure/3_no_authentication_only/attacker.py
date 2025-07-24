import argparse

from config import DEFAULT_HOST

from utils.aes_utils import encrypt
from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

fake_plaintext = "username=bob&action=transfer&amount=999999"

ciphertext_hex = encrypt(fake_plaintext, return_hex=True)

response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=fake_plaintext,
    payload=ciphertext_hex,
    verbose=True
)

print()
