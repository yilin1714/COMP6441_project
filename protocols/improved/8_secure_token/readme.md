# 🔐 HMAC-Signed Secure Token (Stage 8 - Stateless Auth)

This module introduces **stateless authentication** using secure HMAC-signed tokens.
Unlike session IDs stored on the server, these tokens are self-contained and verifiable
without server-side state tracking.

---

## 📘 Overview

In this stage:

- The **client** sends an `init` request with username and password.
- The **server** verifies the credentials and issues a signed token.
- This token includes the username and timestamp, signed with HMAC-SHA256.
- The **client** includes this token in all future requests.
- The **server** verifies the token using the shared secret.
- The **attacker** attempts to omit or forge tokens.

---

## ✅ Improvements Introduced

- ✅ Stateless token-based authentication (no session tracking needed).
- ✅ HMAC-SHA256 protects token integrity.
- ✅ Tokens embed identity and timestamp.
- ✅ Prevents session hijacking without a valid token.

---

## ⚠️ Remaining Vulnerabilities

- ❌ Tokens are not encrypted (can be read in transit).
- ❌ Tokens never expire (timestamp not validated yet).
- ❌ No replay protection (token can be reused).
- ❌ No role-based access or authorization checks.

---

## 🔁 Token Authentication Flow

1. Client sends login request:
   ```
   action=init&username=alice&password=123456
   ```

2. Server responds with a signed token:
   ```
   🔑 Login successful. Your token: alice.1721459033.d3f2eab2378c...
   ```

3. Client sends transaction:
   ```
   token=alice.1721459033.d3f2eab2378c...&action=transfer&amount=1000
   ```

4. Server validates token and replies:
   ```
   ✅ Verified token for 'alice'. Action 'transfer' with amount $1000 accepted.
   ```

---

## 🧪 Example (Benign Client)

Login:
```
action=init&username=alice&password=123456
```

Transaction:
```
token=alice.1721459033.d3f2eab2378c...&action=transfer&amount=1000
```

---

## 💥 Example (Attacker Attempts)

- ❌ No token:
  ```
  [!] Missing token.
  ```

- ❌ Forged token:
  ```
  token=hacker.9999999999.fakehmacsignature
  → [!] Token validation failed: Invalid token signature.
  ```

---

## 🧑‍💻 Module Components

- `client.py`: Logs in and sends authenticated requests with signed token.
- `improved_server.py`: Issues and validates HMAC tokens statelessly.
- `attacker.py`: Sends requests with missing or fake tokens.

---

## 🎓 Educational Purpose

This stage demonstrates the use of **self-contained authentication tokens**
secured via HMAC signatures. It mimics core principles of JWT-style stateless
authentication systems, highlighting both their power and limitations.

---