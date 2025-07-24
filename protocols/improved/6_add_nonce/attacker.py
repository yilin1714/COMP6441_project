import time
import argparse

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port

plain_text = "username=alice&action=transfer&amount=1000&nonce=replay999"
message = plain_text

for i in range(3):
    print(f"\n🔁 Replay Attempt {i + 1}")

    response = run_tcp_attack(
        host=server_host,
        port=server_port,
        plain_text=plain_text,
        payload=message,
        verbose=True
    )

    if i < 2:
        time.sleep(1.2)

print()
