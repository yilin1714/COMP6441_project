import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

used_nonces = set()


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)

        nonce = params.get("nonce")
        if not nonce:
            return "❌ Missing nonce. Request rejected."

        if nonce in used_nonces:
            return f"❌ Replay detected. Nonce '{nonce}' has already been used."

        used_nonces.add(nonce)

        username = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Action '{action}' by '{username}' with amount ${amount} accepted."
    except Exception as e:
        return f"❌ Error parsing request: {e}"


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
