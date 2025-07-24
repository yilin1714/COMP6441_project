import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack
from utils.mac_utils import compute_mac

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to attack")
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

host = args.host
port = args.port

payload1 = "username=intruder&action=withdraw&amount=5000"
run_tcp_attack(
    host=host,
    port=port,
    plain_text=payload1,
    payload=payload1,
    verbose=True
)
time.sleep(0.5)

payload2 = "username=intruder&action=withdraw&amount=5000&mac=deadbeef"
run_tcp_attack(
    host=host,
    port=port,
    plain_text=payload2,
    payload=payload2,
    verbose=True
)
time.sleep(0.5)

original = "username=alice&action=transfer&amount=1000"
valid_mac = compute_mac(original)
tampered = "username=alice&action=transfer&amount=9000&mac=" + valid_mac
run_tcp_attack(
    host=host,
    port=port,
    plain_text=tampered,
    payload=tampered,
    verbose=True
)

print()
