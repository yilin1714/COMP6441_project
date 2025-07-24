# 🧾 Predictable Token

This module demonstrates a session-based authentication system that uses **predictable session IDs**. It shows how an attacker can exploit the predictability to impersonate legitimate users and perform unauthorized actions.

## 📘 Overview

In this demo:
- The **client** sends a request using a known valid `session_id`.
- The **server** checks the `session_id` against a hardcoded database and approves the request.
- The **attacker** brute-forces session IDs in a numeric range and succeeds once it guesses a valid one.

## 🔐 Vulnerabilities Demonstrated

- **Predictable Session IDs**: Tokens follow an easily guessable pattern like incremental integers.
- **No Expiry or Rotation**: Tokens remain valid indefinitely.
- **No Rate Limiting**: Server does not detect or block repeated guessing attempts.
- **No Authentication Binding**: The token alone is enough to impersonate a user.

## 🎯 Message Format

```
session_id=<id>&action=<action>&amount=<value>
```

## 🧪 Example (Benign Client)

Request:
```
session_id=123456&action=transfer&amount=500
```

Response:
```
✅ Session '123456' recognized as 'alice'. transfer of $500 approved.
```

## 💥 Example (Attacker Brute-Force)

Guess:
```
session_id=123457&action=transfer&amount=999999
```

Response:
```
✅ Session '123457' recognized as 'bob'. transfer of $999999 approved.
```

## 🧑‍💻 Module Components

- `client.py`: Sends a valid request using a known session ID via `client_runner`.
- `attacker.py`: Iteratively guesses session IDs using `run_tcp_attacker`.
- `server.py`: Accepts known session IDs using `server_runner` and responds accordingly.

## 🎓 Educational Purpose

This module teaches:
- Why session tokens must be cryptographically unpredictable
- How brute-force enumeration can defeat weak token systems
- The importance of rate limiting and token validation strategy