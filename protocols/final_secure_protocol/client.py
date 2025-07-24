import argparse
import time

from config import DEFAULT_HOST
from shared.crypto_utils import aes_encrypt, hmac_sign
from shared.auth_utils import generate_nonce, hash_password
from shared.config import AES_KEY, HMAC_KEY, PASSWORD_SALT
from utils.client_runner import run_tcp_client


def login(username: str, password: str, server_host: str, server_port: int) -> str:
    print("\n[Client] Logging in...")

    payload = {
        "action": "login",
        "username": username,
        "password": hash_password(password, PASSWORD_SALT),
        "nonce": generate_nonce()
    }

    plaintext = "&".join(f"{k}={v}" for k, v in payload.items())
    encrypted = aes_encrypt(plaintext, AES_KEY)

    response = run_tcp_client(
        host=server_host,
        port=server_port,
        plain_text=plaintext,
        message=encrypted,
        verbose=True
    )

    return response.strip()  # token str


def send_secure_action(token: str, action: str, amount: int, host: str, port: int):
    if not token:
        print("❌ No token provided. Please login first.")
        return

    payload = {
        "action": action,
        "amount": amount,
        "nonce": generate_nonce()
    }

    payload_str = "&".join(f"{k}={v}" for k, v in payload.items())
    payload_str = f"token={token}&{payload_str}"

    mac = hmac_sign(payload_str, HMAC_KEY)

    plaintext = f"{payload_str}&mac={mac}"
    encrypted = aes_encrypt(plaintext, AES_KEY)

    run_tcp_client(
        host=host,
        port=port,
        plain_text=plaintext,
        message=encrypted,
        verbose=True
    )


parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True, help="Port to connect to")
args = parser.parse_args()

server_host = DEFAULT_HOST
server_port = args.port
username = "alice"
password = "123456"
action = "transfer"
amount = 1000

token_cache = None

while True:
    print("\n[💡 Client] Choose an action:")
    print("1️⃣  Login only")
    print("2️⃣  Send secure action (provide token manually)")
    print("3️⃣  Login + Send secure action")
    print("0️⃣  Exit")

    choice = input("\nEnter choice ➤ ").strip()

    if choice == "1":
        token_cache = login(username, password, server_host, server_port)
        time.sleep(0.5)

    elif choice == "2":
        send_secure_action(token_cache, action, amount, server_host, server_port)
        time.sleep(0.5)

    elif choice == "3":
        token_cache = login(username, password, server_host, server_port)
        time.sleep(1)
        send_secure_action(token_cache, action, amount, server_host, server_port)
        time.sleep(0.5)

    elif choice == "0":
        print("👋 Exiting client.")
        break

    else:
        print("❌ Invalid input. Please choose 1, 2, 3, or 0.")
