import argparse

from config import DEFAULT_HOST

from utils.aes_utils import decrypt
from utils.notifier import notify_ready
from utils.parser_utils import parse_kv_string
from utils.server_runner import run_tcp_server


def handle_request(ciphertext_hex: str) -> str:
    decrypted = decrypt(ciphertext_hex)
    if decrypted.startswith("[!]"):
        return f"❌ Error: {decrypted}"

    print(f"   Decrypted message: {decrypted}")
    params = parse_kv_string(decrypted)

    user = params.get("username", "unknown")
    action = params.get("action", "none")
    amount = params.get("amount", "0")

    return f"✅ Action '{action}' by '{user}' for ${amount} accepted."


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to bind the server on")
parser.add_argument("--notify-port", type=int, required=False, help="Optional notify port for run_demo")
args = parser.parse_args()

run_tcp_server(
    port=args.port,
    handle_request=handle_request,
    host=DEFAULT_HOST,
    on_ready=(lambda: notify_ready(args.notify_port)) if args.notify_port else None
)
