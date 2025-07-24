# 🔐 Final Secure Protocol

This is the final stage of the secure communication protocol project, implementing a secure-by-design client-server protocol resistant to common network attacks such as:

- 🧑‍💻 Credential theft
- 🔁 Replay attacks
- 🛠 Forged or tampered messages
- 🎭 Session hijacking

---

## ✅ Key Features

- **AES-CBC encryption** with PKCS7 padding for message confidentiality.
- **HMAC-SHA256** for integrity and authenticity of each message.
- **Nonce mechanism** to prevent replay attacks (nonces are checked and stored).
- **Token-based authentication** with expiration to avoid credential reuse.
- **Session binding** for actions, tightly coupling token + nonce + payload.

---

## 📁 Files

| File                      | Description                                  |
|---------------------------|----------------------------------------------|
| `improved_server.py`      | Final server implementation with full checks |
| `secure_client.py`        | Client that handles encryption, signing, and session |
| `attacker.py`             | Simulated attacker to test replay/hijack     |
| `shared/config.py`        | Keys, token expiry, nonce cache, user DB     |
| `shared/crypto_utils.py`  | AES/HMAC utilities                           |
| `shared/nonce_utils.py`   | Nonce checking and storing functions         |
| `shared/token_utils.py`   | Token generation and validation              |

---

## 🧪 How It Works

### 🔑 Login Flow

1. Client sends:  
   `{ username, password_hash, nonce }`

2. Server:
   - Verifies password
   - Checks replayed nonce
   - Generates signed + encrypted token
   - Returns token to client

---

### 📤 Transaction Flow

1. Client sends (as key-value string):
   ```
   token=<base64_encoded_json>&action=transfer&amount=100&nonce=unique123
   ```

2. Server:
   - Verifies HMAC signature
   - Decrypts token and checks expiry
   - Validates nonce again (for action)
   - Accepts or rejects the request

---

## 🧠 Security Lessons

- **Encryption ≠ secure** — authentication and freshness are also essential.
- **Replay protection** is crucial in real-world protocols like OAuth and SWIFT.
- **MAC before encryption (and check first!)** — ensures message integrity.
- **Tokens should expire** — long-lived tokens are vulnerable if leaked.

---

## 🛡️ Final Outcome

This protocol satisfies **Confidentiality**, **Integrity**, and **Authentication** requirements and is robust against attacks demonstrated in earlier stages.