import argparse
import time

from config import DEFAULT_HOST
from utils.attacker_runner import run_tcp_attack


def attack_missing_session(host, port):
    print("\n[Attack 1] Sending request WITHOUT session_id...")
    plain = "username=admin&action=steal&amount=999999"
    run_tcp_attack(host, port, plain, plain, verbose=True)


def attack_fake_session(host, port):
    print("\n[Attack 2] Sending request with FAKE session_id...")
    plain = "session_id=notarealsession123&username=hacker&action=withdraw&amount=888888"
    run_tcp_attack(host, port, plain, plain, verbose=True)


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

attack_missing_session(args.host, args.port)
time.sleep(0.8)
attack_fake_session(args.host, args.port)

print()
