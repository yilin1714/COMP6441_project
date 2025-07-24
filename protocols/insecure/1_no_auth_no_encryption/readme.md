# 📡 No Auth, No Encryption

This module demonstrates an insecure TCP-based protocol where both authentication and encryption are completely missing. It serves as the baseline for comparing more advanced protocols and highlights the critical importance of even basic security protections.

## 📘 Overview

In this demo:
- The **client** sends a sensitive operation in **plaintext**.
- The **server** blindly accepts the request and returns a confirmation.
- The **attacker** can easily replay or modify requests to impersonate others or perform unauthorized actions.

## 🔐 Vulnerabilities Demonstrated

- **No Authentication**: Any client (including attackers) can send a valid request.
- **No Encryption**: Requests are visible and modifiable in transit.
- **No Input Validation or Integrity Check**: The server parses and trusts any input that conforms to the basic format.

## 🎯 Message Format

Requests follow the form:
```
username=<name>&action=<action>&amount=<value>
```

The server parses this and accepts the operation without further validation.

## 🧪 Example (Benign Client)

```
username=alice&action=transfer&amount=1000
```

Server responds:
```
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
```

## 💥 Example (Attacker Exploit)

```
username=admin&action=transfer&amount=999999
```

Server responds:
```
✅ Action 'transfer' by 'admin' with amount $999999 accepted.
```

## 🧑‍💻 Module Components

- `client.py`: Sends a hardcoded transaction request in plaintext using `client_runner`.
- `attacker.py`: Replays or modifies the message to perform a forged transaction.
- `server.py`: Uses `server_runner` to receive, parse, and blindly accept messages.

## 🎓 Educational Purpose

This example sets the stage for understanding:
- Why encryption alone is not enough
- Why identity/authentication checks matter
- How easy it is to exploit unauthenticated, unprotected protocols