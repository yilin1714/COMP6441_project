import argparse
import random
import string

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client


def generate_nonce(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
parser.add_argument("--nonce", type=str, help="Optional fixed nonce for replay testing")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

nonce = args.nonce if args.nonce else generate_nonce()
plain_text = f"username=alice&action=transfer&amount=1000&nonce={nonce}"

response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=plain_text,
    verbose=True
)

print()
