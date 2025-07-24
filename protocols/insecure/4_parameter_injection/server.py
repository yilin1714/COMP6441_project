import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(raw_data: str) -> str:
    try:
        params = parse_kv_string(raw_data)
        user = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        response = f"✅ Action '{action}' by '{user}' for ${amount} accepted."
        return response

    except Exception as e:
        error_msg = f"❌ Error parsing request: {e}"
        return error_msg


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number to bind the server")
parser.add_argument("--notify-port", type=int, required=False, help="Optional port to notify when ready")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
