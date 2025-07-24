import argparse
import time
import hmac
import hashlib

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server

USER_DB = {
    "alice": "123456",
    "bob": "secretpass",
    "charlie": "qwerty"
}

TOKEN_SECRET = b"SuperSecretKey"


def generate_token(username: str) -> str:
    timestamp = str(int(time.time()))
    message = f"{username}.{timestamp}"
    signature = hmac.new(TOKEN_SECRET, message.encode(), hashlib.sha256).hexdigest()
    return f"{username}.{timestamp}.{signature}"


def validate_token(token: str) -> str:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid token format.")
        username, timestamp, provided_sig = parts
        message = f"{username}.{timestamp}"
        expected_sig = hmac.new(TOKEN_SECRET, message.encode(), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(provided_sig, expected_sig):
            raise ValueError("Invalid token signature.")

        return username
    except Exception as e:
        raise ValueError(f"Token validation failed: {e}")


def handle_request(data: str) -> str:
    try:
        params = parse_kv_string(data)
        action = params.get("action")

        if action == "init":
            username = params.get("username")
            password = params.get("password")
            if USER_DB.get(username) != password:
                return "[!] Invalid username or password."
            token = generate_token(username)
            return f"🔑 Login successful. Your token: {token}"

        token = params.get("token")
        if not token:
            return "[!] Missing token."

        try:
            username = validate_token(token)
        except ValueError as e:
            return f"[!] {e}"

        action = params.get("action", "none")
        amount = params.get("amount", "0")

        return f"✅ Verified token for '{username}'. Action '{action}' with amount ${amount} accepted."

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
