import argparse

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client


def request_session_id(host, port) -> str:
    init_plain = "action=init"

    print("\n[Step 1] Requesting session_id from server...")
    response = run_tcp_client(
        host=host,
        port=port,
        plain_text=init_plain,
        message=init_plain,
        verbose=True
    )
    print()

    if response and "Your session_id:" in response:
        try:
            return response.split("Your session_id:")[-1].strip()
        except Exception:
            return ""
    return ""


def send_transaction(session_id, host, port):
    plain = f"session_id={session_id}&username=alice&action=transfer&amount=1000"

    print("[Step 2] Sending transaction request...")
    run_tcp_client(
        host=host,
        port=port,
        plain_text=plain,
        message=plain,
        verbose=True
    )
    print()


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Target host")
args = parser.parse_args()

sid = request_session_id(args.host, args.port)
if sid:
    send_transaction(sid, args.host, args.port)
else:
    print("[Client] ❌ Failed to obtain session_id.")
