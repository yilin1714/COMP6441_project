import base64
import argparse

from config import DEFAULT_HOST

from utils.client_runner import run_tcp_client

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=alice&action=transfer&amount=1000"

encoded = base64.b64encode(plain_text.encode()).decode()

response = run_tcp_client(server_host, server_port, plain_text, encoded, verbose=True)

print()
