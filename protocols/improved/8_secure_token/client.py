import argparse
import time

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client


def request_token(host, port, username, password):
    login_msg = f"action=init&username={username}&password={password}"
    print("\n[Step 1] Logging in to receive secure token...")

    response = run_tcp_client(
        host=host,
        port=port,
        plain_text=login_msg,
        message=login_msg,
        verbose=True
    )
    print()

    if response and "Your token:" in response:
        try:
            return response.split("Your token:")[-1].strip()
        except Exception:
            return None
    return None


def send_transaction(host, port, token):
    tx_msg = f"token={token}&action=transfer&amount=1000"
    print("[Step 2] Sending transaction with token...")

    run_tcp_client(
        host=host,
        port=port,
        plain_text=tx_msg,
        message=tx_msg,
        verbose=True
    )
    print()


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--host", type=str, default=DEFAULT_HOST)
args = parser.parse_args()

username = "alice"
password = "123456"

token = request_token(args.host, args.port, username, password)
time.sleep(1)

if token:
    send_transaction(args.host, args.port, token)
else:
    print("[Client] ❌ Failed to obtain valid token.")
