

import argparse

from config import DEFAULT_HOST
from utils.mac_utils import compute_mac
from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Server host")
args = parser.parse_args()

message = "username=alice&action=transfer&amount=1000"
mac = compute_mac(message)
full_message = f"{message}&mac={mac}"

response = run_tcp_client(
    host=args.host,
    port=args.port,
    plain_text=message,
    message=full_message,
    verbose=True
)
print()
