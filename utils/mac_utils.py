import hmac
import hashlib
from typing import Tuple

MAC_KEY = b"MACSecretKey4567"


def compute_mac(message: str) -> str:
    return hmac.new(MAC_KEY, message.encode("utf-8"), hashlib.sha256).hexdigest()


def verify_mac(message_with_mac: str) -> Tuple[bool, str]:
    if "&mac=" not in message_with_mac:
        return False, "[!] MAC missing."

    try:
        message, received_mac = message_with_mac.rsplit("&mac=", 1)
        expected_mac = compute_mac(message)

        if hmac.compare_digest(received_mac, expected_mac):
            return True, message
        else:
            return False, "[!] MAC verification failed."
    except Exception as e:
        return False, f"[!] MAC verification error: {e}"
