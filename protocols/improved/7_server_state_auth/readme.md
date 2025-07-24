

# 🔐 Username + Password Auth (Stage 7 - Server-Side Authenticated Session)

This module introduces **server-side authentication** using username and password.
Clients must first log in with credentials to obtain a session ID. All future requests
must include that session ID, which the server checks for validity and authentication state.

---

## 📘 Overview

In this stage:

- The **client** sends `action=init` with `username` and `password`.
- The **server** checks the credentials and returns a random `session_id`.
- The session is bound to the authenticated user on the server side.
- Future client requests must include the `session_id`.
- The **attacker** tries to forge or omit session IDs.

---

## ✅ Improvements Introduced

- ✅ Enforces user authentication before any action is allowed.
- ✅ Session IDs are securely generated (UUIDv4) and bound to specific users.
- ✅ Prevents unauthorized or unauthenticated access.
- ✅ Distinguishes between authenticated and unauthenticated sessions.

---

## ⚠️ Remaining Vulnerabilities

- ❌ No encryption: usernames and passwords are sent in plaintext.
- ❌ No integrity protection (MAC, signature).
- ❌ No replay protection (e.g., nonce/timestamp).

---

## 🔁 Authentication Flow

1. Client sends:
   ```
   action=init&username=alice&password=123456
   ```

2. Server responds:
   ```
   🎯 Authenticated. Your session_id: 54cdd3e76a4e4bdbb341bf020ab2d8c7
   ```

3. Client sends:
   ```
   session_id=54cdd3e76a4e4bdbb341bf020ab2d8c7&action=transfer&amount=1000
   ```

4. Server verifies the session is authenticated and responds:
   ```
   ✅ Authenticated as 'alice'. Action 'transfer' for $1000 accepted.
   ```

---

## 🧪 Example (Benign Client)

Login request:
```
action=init&username=alice&password=123456
```

Transaction request:
```
session_id=...&action=transfer&amount=1000
```

---

## 💥 Example (Attacker Attempts)

- ❌ Missing session_id:
  ```
  [!] Invalid or unauthenticated session_id.
  ```

- ❌ Forged session_id:
  ```
  [!] Invalid or unauthenticated session_id.
  ```

---

## 🧑‍💻 Module Components

- `client.py`: Logs in with credentials and performs a transaction using session_id.
- `improved_server.py`: Validates credentials, issues session_ids, and enforces authentication state.
- `attacker.py`: Attempts to bypass authentication or forge sessions.

---

## 🎓 Educational Purpose

This module demonstrates the importance of authenticating users before allowing access to operations.
It also highlights how session management can enforce persistent authentication across multiple requests.

---
