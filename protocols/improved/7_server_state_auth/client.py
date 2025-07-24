import argparse
import time

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client


def request_session_id(host, port, username, password):
    login_msg = f"action=init&username={username}&password={password}"
    print("\n[Step 1] Logging in...")

    response = run_tcp_client(
        host=host,
        port=port,
        plain_text=login_msg,
        message=login_msg,
        verbose=True
    )
    print()

    if response and "session_id" in response:
        try:
            return response.split(":")[-1].strip()
        except Exception:
            return None
    return None


def send_transaction(host, port, session_id):
    tx_msg = f"session_id={session_id}&action=transfer&amount=1000"
    print("[Step 2] Sending transaction...")

    run_tcp_client(
        host=host,
        port=port,
        plain_text=tx_msg,
        message=tx_msg,
        verbose=True
    )
    print()


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target server port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Server host")
args = parser.parse_args()

username = "alice"
password = "123456"

session_id = request_session_id(args.host, args.port, username, password)
time.sleep(1)

if session_id:
    send_transaction(args.host, args.port, session_id)
else:
    print("[Client] ❌ Login failed or session_id not returned.")
