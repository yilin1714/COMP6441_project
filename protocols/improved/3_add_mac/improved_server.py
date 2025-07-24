
import argparse

from config import DEFAULT_HOST
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server
from utils.mac_utils import verify_mac

def handle_request(data: str) -> str:

    ok, result = verify_mac(data)
    if not ok:
        return result

    params = parse_kv_string(result)
    username = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Verified. Action '{action}' by '{username}' with amount ${amount} accepted."


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port number to bind to")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)