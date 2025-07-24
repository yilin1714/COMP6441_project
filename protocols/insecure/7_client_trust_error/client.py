import argparse

from config import DEFAULT_HOST

from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=alice&balance=100&action=withdraw"
message = plain_text

response = run_tcp_client(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    message=message,
    verbose=True
)

print()
