# final_secure_protocol/attacker.py

"""
attacker.py - Final Secure Protocol Attacker (Interactive)

Simulates different types of attacks against the secure server:
- 1️⃣ No token
- 2️⃣ Forged token
- 3️⃣ Replay attack (requires real token + nonce)
- 4️⃣ Tampered payload
"""

import argparse
import json
import time

from config import DEFAULT_HOST
from shared.crypto_utils import aes_encrypt, hmac_sign
from shared.auth_utils import generate_nonce
from shared.config import AES_KEY, HMAC_KEY
from utils.attacker_runner import run_tcp_attack


def attack_no_token(host, port):
    print("\n[🚨 Attack 1️⃣] No token provided")

    # 构造 payload（没有 token）
    payload = {
        "action": "transfer",
        "amount": 9999,
        "nonce": generate_nonce()
    }
    payload_str = "&".join(f"{k}={v}" for k, v in payload.items())
    mac = hmac_sign(payload_str, HMAC_KEY)
    full_str = f"{payload_str}&mac={mac}"

    encrypted = aes_encrypt(full_str, AES_KEY)

    run_tcp_attack(host, port, plain_text=full_str, payload=encrypted, verbose=True)


def attack_forged_token(host, port):
    print("\n[🚨 Attack 2️⃣] Forged token")

    # 构造一个假的未加密 token 字符串
    forged_token_fields = {
        "username": "alice",
        "exp": 9999999999
    }
    token_payload = "&".join(f"{k}={v}" for k, v in forged_token_fields.items())
    fake_sig = "deadbeef" * 8
    forged_token = f"{token_payload}&sig={fake_sig}"

    # 构造交易请求
    payload = {
        "token": aes_encrypt(forged_token, AES_KEY),
        "action": "transfer",
        "amount": 1000000,
        "nonce": generate_nonce()
    }
    payload_str = "&".join(f"{k}={v}" for k, v in payload.items())
    mac = hmac_sign(payload_str, HMAC_KEY)
    full_str = f"{payload_str}&mac={mac}"

    encrypted = aes_encrypt(full_str, AES_KEY)

    run_tcp_attack(host, port, plain_text=full_str, payload=encrypted, verbose=True)


def attack_replay(host, port):
    print("\n[🚨 Attack 3️⃣] Replay attack")

    token = input("Paste a real token ➤ ").strip()
    nonce = input("Paste the original nonce ➤ ").strip()
    mac = input("Paste the original mac ➤ ").strip()

    payload = {
        "token": token,
        "action": "transfer",
        "amount": 1000,
        "nonce": nonce
    }
    payload_str = "&".join(f"{k}={v}" for k, v in payload.items())
    full_str = f"{payload_str}&mac={mac}"

    encrypted = aes_encrypt(full_str, AES_KEY)

    run_tcp_attack(host, port, plain_text=full_str, payload=encrypted, verbose=True)


def attack_tampered_payload(host, port):
    print("\n[🚨 Attack 4️⃣] Tampered payload after signing")

    token = input("Paste a real token ➤ ").strip()

    # 正常构造并签名
    payload = {
        "token": token,
        "action": "transfer",
        "amount": 1000,
        "nonce": generate_nonce()
    }
    original_str = "&".join(f"{k}={v}" for k, v in payload.items())
    mac = hmac_sign(original_str, HMAC_KEY)

    # 篡改 amount
    payload["amount"] = 999999
    tampered_str = "&".join(f"{k}={v}" for k, v in payload.items())
    full_str = f"{tampered_str}&mac={mac}"

    encrypted = aes_encrypt(full_str, AES_KEY)

    run_tcp_attack(host, port, plain_text=full_str, payload=encrypted, verbose=True)


# --- Entry Point ---
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()

host = DEFAULT_HOST
port = args.port

# --- Interactive Menu ---
while True:
    print("\n[🛡️ Final Secure Protocol - Attacker Menu]")
    print("1️⃣  No token provided")
    print("2️⃣  Forged token")
    print("3️⃣  Replay attack (manual token & nonce)")
    print("4️⃣  Tampered payload after signing")
    print("5️⃣  Exit")

    choice = input("\nEnter attack number to launch ➤ ").strip()

    if choice == "1":
        attack_no_token(host, port)
        time.sleep(0.5)

    elif choice == "2":
        attack_forged_token(host, port)
        time.sleep(0.5)

    elif choice == "3":
        attack_replay(host, port)
        time.sleep(0.5)

    elif choice == "4":
        attack_tampered_payload(host, port)
        time.sleep(0.5)

    elif choice == "5":
        print("👋 Exiting attacker.")
        break
    else:
        print("❌ Invalid choice. Try again.")
