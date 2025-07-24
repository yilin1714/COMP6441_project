import argparse

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Target host")
args = parser.parse_args()

message = "username=alice&action=transfer&amount=1000"

response = run_tcp_client(
    host=args.host,
    port=args.port,
    plain_text=message,
    message=message,
    verbose=True
)
print()
