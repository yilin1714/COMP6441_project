from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from typing import Union

from config import AES_KEY, AES_IV

KEY = AES_KEY
IV = AES_IV


def encrypt(plaintext: str, return_hex: bool = False) -> Union[bytes, str]:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded = pad(plaintext.encode("utf-8"), AES.block_size)
    ciphertext = cipher.encrypt(padded)
    return ciphertext.hex() if return_hex else ciphertext


def decrypt(ciphertext: Union[bytes, str]) -> str:
    if isinstance(ciphertext, str):
        try:
            ciphertext = bytes.fromhex(ciphertext)
        except ValueError:
            return "[!] Invalid hex string for ciphertext."

    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    try:
        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, AES.block_size).decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        return "[!] Decryption failed or message is corrupted."


if __name__ == "__main__":
    message = "username=alice&action=transfer&amount=1000"
    print("🔓 Plaintext:", message)

    encrypted = encrypt(message, return_hex=True)
    print("🔐 Encrypted (hex):", encrypted)

    decrypted = decrypt(encrypted)
    print("✅ Decrypted:", decrypted)

    print("⚠️  WARNING: This encryption demo uses a static key and IV with no authentication.")
    print("⚠️  DO NOT use this implementation in any real-world or production scenario.")
