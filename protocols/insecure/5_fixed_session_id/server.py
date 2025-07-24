import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

session_store = {
    "abc123": "alice",
    "xyz789": "bob"
}


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)
        sid = params.get("session_id", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        username = session_store.get(sid, None)

        if username:
            response = f"✅ Session '{sid}' identified as '{username}': action '{action}' of ${amount} accepted."
            return response

        else:
            response = f"❌ Invalid session_id."
            return response

    except Exception as e:
        error_msg = f"❌ Request error: {e}"
        return error_msg


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
