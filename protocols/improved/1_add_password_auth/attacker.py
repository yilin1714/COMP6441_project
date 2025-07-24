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

response = run_tcp_attack(
    host=server_host,
    port=server_port,
    plain_text=plain_text,
    payload=payload,
    verbose=True
)
print()
