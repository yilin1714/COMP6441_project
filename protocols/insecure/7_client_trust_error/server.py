import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

real_balance = {
    "alice": 100
}


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)
        username = params.get("username")
        claimed_balance = params.get("balance")
        action = params.get("action")

        return f"✅ {username} requested '{action}' with claimed balance ${claimed_balance}. Accepted!"

    except Exception as e:
        return f"❌ Error: {e}"


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
