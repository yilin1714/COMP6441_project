# 🔒 Base64 Fake Encryption

This module demonstrates an insecure protocol that **uses Base64 encoding as a substitute for encryption**. It highlights how encoding provides no true confidentiality and can give developers a false sense of security.

## 📘 Overview

In this demo:
- The **client** sends a Base64-encoded message that appears "encrypted".
- The **server** simply decodes the message and accepts it.
- The **attacker** can forge or tamper with encoded messages because Base64 is fully reversible.

## 🔐 Vulnerabilities Demonstrated

- **Fake Encryption**: Base64 is reversible and not secure; anyone can decode the message.
- **No Authentication**: No mechanism is used to verify the sender's identity.
- **No Integrity Checks**: Modified or forged messages are accepted without validation.
- **Misleading Design**: Developers may believe Base64 adds protection, when it does not.

## 🎯 Message Format

Messages are constructed in the following plaintext format:
```
username=<name>&action=<action>&amount=<value>
```
The client encodes the message using Base64 before sending, and the server decodes and processes it as-is.

## 🧪 Example (Benign Client)

Plaintext:
```
username=alice&action=transfer&amount=1000
```

Encoded:
```
dXNlcm5hbWU9YWxpY2UmYWN0aW9uPXRyYW5zZmVyJmFtb3VudD0xMDAw
```

Server responds:
```
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
```

## 💥 Example (Attacker Exploit)

Modified plaintext:
```
username=admin&action=transfer&amount=999999
```

Encoded:
```
dXNlcm5hbWU9YWRtaW4mYWN0aW9uPXRyYW5zZmVyJmFtb3VudD05OTk5OTk=
```

Server responds:
```
✅ Action 'transfer' by 'admin' with amount $999999 accepted.
```

## 🧑‍💻 Module Components

- `client.py`: Encodes a transaction request with Base64 and sends it using `client_runner`.
- `attacker.py`: Decodes a legitimate message, modifies it, re-encodes and sends it.
- `server.py`: Uses `server_runner` to receive, decode, and process Base64-encoded messages.

## 🎓 Educational Purpose

This module teaches:
- Encoding ≠ Encryption
- Why real encryption must include confidentiality + authenticity
- The risks of trusting unverified, trivially decodable input
