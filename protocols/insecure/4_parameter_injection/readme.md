# 🧩 Parameter Injection (No Auth, No Validation)

This module demonstrates how insecure input handling can be exploited when a server blindly parses untrusted parameters. It highlights the risks of using `key=value&...` formatted strings without input validation or authentication.

## 📘 Overview

In this demo:
- The **client** sends a plaintext key-value message (e.g., `username=alice&...`) directly to the server.
- The **server** parses the input using `split()` and accepts any keys or values without checking their legitimacy.
- The **attacker** modifies or injects new parameters (e.g., `admin=true`) and sends them to the server.

## 🔐 Vulnerabilities Demonstrated

- **Parameter Injection**: Attacker can introduce arbitrary keys to trigger unintended logic (e.g., `admin=true`).
- **No Authentication**: Server accepts messages from any sender without verifying identity.
- **No Integrity**: Tampered messages are blindly accepted.

## 🎯 Message Format

Plaintext messages follow:
```
username=<name>&action=<action>&amount=<value>
```

The server blindly parses this format into parameters.

## 🧪 Example (Benign Client)

```
username=alice&action=transfer&amount=1000
```

Server responds:
```
✅ Action 'transfer' by 'alice' for $1000 accepted.
```

## 💥 Example (Attacker Exploit)

Injected message:
```
username=attacker&action=transfer&amount=999999&admin=true
```

Server still responds:
```
✅ Action 'transfer' by 'attacker' for $999999 accepted.
```

## 🧑‍💻 Module Components

- `client.py`: Sends a legitimate request using `client_runner`, with verbose logging.
- `attacker.py`: Sends a forged message with injected fields (e.g., `admin=true`) using `attacker_runner`.
- `server.py`: Uses `server_runner` to receive and parse incoming messages without validating keys.

## 🎓 Educational Purpose

This module teaches:
- The danger of trusting user input without validation.
- How protocol parsers can be exploited by malicious input.
- Why input sanitization, authentication, and message integrity are critical.