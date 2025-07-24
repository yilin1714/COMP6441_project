import argparse
import uuid

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

active_sessions = set()


def generate_session_id() -> str:
    sid = uuid.uuid4().hex
    active_sessions.add(sid)
    return sid


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)

        if params.get("action") == "init":
            sid = generate_session_id()
            return f"🎯 Your session_id: {sid}"

        session_id = params.get("session_id")
        if session_id not in active_sessions:
            return "[!] Invalid or missing session_id."

        username = params.get("username", "unknown")
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Session verified. Action '{action}' by '{username}' with amount ${amount} accepted."

    except Exception as e:
        return f"[!] Error processing request: {e}"


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
