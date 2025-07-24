"""
client.py - Plaintext Session ID Client (Stage 5)

This client first requests a session ID from the server using `action=init`,
then uses that session_id in a plaintext transaction request.

No encryption or HMAC is used.

Usage:
    python client.py --port 9000
"""

import argparse

from config import DEFAULT_HOST
from utils.client_runner import run_tcp_client

# Step 1: Request session ID (plaintext)
def request_session_id(host, port) -> str:
    init_plain = "action=init"

    print("\n[Step 1] Requesting session_id from server...")
    response = run_tcp_client(
        host=host,
        port=port,
        plain_text=init_plain,
        message=init_plain,
        verbose=True
    )
    print()

    # More robust: look for the phrase "Your session_id:"
    if response and "Your session_id:" in response:
        try:
            return response.split("Your session_id:")[-1].strip()
        except Exception:
            return ""
    return ""

# Step 2: Use session_id to send transaction
def send_transaction(session_id, host, port):
    plain = f"session_id={session_id}&username=alice&action=transfer&amount=1000"

    print("[Step 2] Sending transaction request...")
    run_tcp_client(
        host=host,
        port=port,
        plain_text=plain,
        message=plain,
        verbose=True
    )
    print()

# --- Main Execution ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Target port")
parser.add_argument("--host", type=str, default=DEFAULT_HOST, help="Target host")
args = parser.parse_args()

sid = request_session_id(args.host, args.port)
if sid:
    send_transaction(sid, args.host, args.port)
else:
    print("[Client] ❌ Failed to obtain session_id.")