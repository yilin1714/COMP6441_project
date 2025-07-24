import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack


def attack_no_session_id(host, port):
    print("\n[Attack 1] No session_id (unauthenticated request)...")
    payload = "username=hacker&action=transfer&amount=999999"
    run_tcp_attack(
        host=host,
        port=port,
        plain_text=payload,
        payload=payload,
        verbose=True
    )


def attack_fake_session_id(host, port):
    print("\n[Attack 2] Forged session_id (unauthorized access)...")
    payload = "session_id=notavalidsession123&username=hacker&action=steal&amount=1000000"
    run_tcp_attack(
        host=host,
        port=port,
        plain_text=payload,
        payload=payload,
        verbose=True
    )


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Target host")
args = parser.parse_args()

attack_no_session_id(args.host, args.port)
time.sleep(1)
attack_fake_session_id(args.host, args.port)
print()
