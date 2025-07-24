# 🪪 Fixed Session ID (No Expiry)

This module demonstrates how insecure session management can allow attackers to impersonate legitimate users. It highlights the danger of using **static session IDs** without expiry, binding, or validation.

## 📘 Overview

In this demo:
- The **client** sends a request with a fixed `session_id`, which the server accepts as proof of identity.
- The **server** uses the `session_id` to look up a username and grants access without checking IP, device, expiry, or authenticity.
- The **attacker** forges a request using the same `session_id`, impersonating the user and executing sensitive actions.

## 🔐 Vulnerabilities Demonstrated

- **Static Session Tokens**: The same session_id can be reused by anyone who knows it.
- **No Expiry or Timeout**: Sessions never expire, allowing long-term misuse.
- **No Binding or Verification**: Session IDs are not tied to client IP, device, or login context.
- **No Integrity**: Requests are not signed or authenticated.

## 🎯 Message Format

Plaintext messages follow:
```
session_id=<token>&action=<action>&amount=<value>
```

The server blindly parses this input and accepts any request if the session ID exists in its in-memory database.

## 🧪 Example (Benign Client)

```
session_id=abc123&action=transfer&amount=1000
```

Server responds:
```
✅ Session 'abc123' identified as 'alice': action 'transfer' of $1000 accepted.
```

## 💥 Example (Attacker Exploit)

```
session_id=abc123&action=transfer&amount=999999
```

Server responds:
```
✅ Session 'abc123' identified as 'alice': action 'transfer' of $999999 accepted.
```

## 🧑‍💻 Module Components

- `client.py`: Sends a fixed-session request using `client_runner`.
- `attacker.py`: Reuses the same session_id with a malicious payload using `attacker_runner`.
- `server.py`: Uses `server_runner` and `session_store` lookup to respond without verification.

## 🎓 Educational Purpose

This module teaches:
- Why sessions must be expirable and bound to context
- The risk of accepting identifiers without verification
- How trivial it is to exploit predictable or long-lived session tokens
