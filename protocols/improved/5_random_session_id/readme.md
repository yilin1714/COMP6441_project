# 🧾 Random Session ID (Stage 5 - Plaintext Session Management)

This module introduces random session IDs in a plaintext protocol.
Clients must first obtain a server-issued `session_id` via an `init` request before making any transaction.
All future requests must include a valid session_id, or the server will reject them.

---

## 📘 Overview

In this stage:
- The **client** must first request a session ID using an `action=init` request.
- The **server** responds with a unique session_id.
- All future requests must include this session_id to be accepted.
- The **attacker** attempts to omit or forge a session_id.

---

## ✅ Improvements Introduced

- ✅ Session IDs are high-entropy UUIDv4 strings.
- ✅ Enforces server-issued session lifecycle.
- ✅ Plaintext validation of session_id for every request.

---

## ⚠️ Remaining Vulnerabilities

- ❌ No encryption: requests are readable and modifiable in transit.
- ❌ No authentication: anyone can request a session_id.
- ❌ No replay prevention (e.g., nonce or timestamp).

---

## 🔐 Session Flow

1. Client sends `action=init`
2. Server returns something like:
   ```
   🎯 Your session_id: 4f8e12c91a33b...
   ```
3. Client sends:
   ```
   session_id=...&username=...&action=...&amount=...
   ```

---

## 🧪 Example (Valid Client Request)

```
session_id=4f8e...&username=alice&action=transfer&amount=1000
```

✅ Server responds:
```
✅ Session verified. Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 💥 Example (Attacker Requests)

- ❌ Missing session_id:
  ```
  [!] Invalid or missing session_id.
  ```

- ❌ Forged session_id:
  ```
  [!] Invalid or missing session_id.
  ```

---

## 🧑‍💻 Module Components

- `client.py`: Requests a session_id, sends plaintext transaction.
- `improved_server.py`: Generates and validates session_id from memory.
- `attacker.py`: Attempts to omit or spoof session_id.

---

## 🎓 Educational Purpose

This module introduces basic **stateful session management**, simulating
authentication tokens and demonstrating how state can enhance protocol control.

---
