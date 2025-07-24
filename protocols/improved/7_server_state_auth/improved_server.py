import argparse
import uuid

from config import DEFAULT_HOST

from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

USER_DB = {
    "alice": "123456",
    "bob": "secretpass",
    "charlie": "qwerty"
}

session_auth_map = {}


def generate_session_id(username=None) -> str:
    sid = uuid.uuid4().hex
    if username:
        session_auth_map[sid] = username
    return sid


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)
        action = params.get("action")

        if action == "init":
            username = params.get("username")
            password = params.get("password")
            if not username or not password:
                return "[!] Username and password required for init."

            if USER_DB.get(username) != password:
                return "[!] Invalid credentials."

            sid = generate_session_id(username)
            return f"🎯 Authenticated. Your session_id: {sid}"

        session_id = params.get("session_id")
        if not session_id or session_id not in session_auth_map:
            return "[!] Invalid or unauthenticated session_id."

        username = session_auth_map[session_id]
        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Authenticated as '{username}'. Action '{action}' for ${amount} accepted."

    except Exception as e:
        return f"[!] Server error: {e}"


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
parser.add_argument("--notify-port", type=int)
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
