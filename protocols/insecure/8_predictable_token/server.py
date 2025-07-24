import argparse

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

session_db = {
    "123456": "alice",
    "123457": "bob"
}


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)
        sid = params.get("session_id")
        action = params.get("action")
        amount = params.get("amount")

        user = session_db.get(sid)

        if user:
            return f"✅ Session '{sid}' recognized as '{user}'. {action} of ${amount} approved."
        else:
            return "❌ Invalid or unknown session_id."
    except Exception as e:
        return f"❌ Error processing request: {e}"


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
