import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="The port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=attacker&action=transfer&amount=999999&admin=true"
malicious_message = "username=attacker&action=transfer&amount=999999&admin=true"

response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=malicious_message,
    verbose=True
)

print()
