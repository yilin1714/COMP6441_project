# 🔒 AES Encryption, No Authentication

This module demonstrates a flawed protocol that uses **AES encryption** to protect messages but **lacks any form of authentication or integrity**. While the message is encrypted, the server cannot verify the sender’s identity or detect tampering.

## 📘 Overview

In this demo:
- The **client** encrypts a sensitive request using AES (CBC mode).
- The **server** decrypts the message using a shared key and executes it without verification.
- The **attacker** can forge and send valid-looking encrypted messages using the same key.

## 🔐 Vulnerabilities Demonstrated

- **No Authentication**: The server blindly trusts any decryptable message.
- **Shared Key Misuse**: Anyone with the key can impersonate legitimate users.
- **No Integrity Check**: The message may be tampered with and still be accepted.
- **No Forward Secrecy**: Reuse of key and IV allows message prediction.

## 🎯 Message Format

The plaintext message follows:
```
username=<name>&action=<action>&amount=<value>
```

This string is AES-encrypted using a shared symmetric key and IV.

## 🧪 Example (Benign Client)

Plaintext:
```
username=alice&action=transfer&amount=1000
```

Encrypted (hex example):
```
13005d9d0a5569ff9ee740d3e3244032...
```

Server responds:
```
✅ Action 'transfer' by 'alice' for $1000 accepted.
```

## 💥 Example (Attacker Exploit)

Forged plaintext:
```
username=bob&action=transfer&amount=999999
```

Encrypted with the same key, sent directly to the server.

Server responds:
```
✅ Action 'transfer' by 'bob' for $999999 accepted.
```

## 🧑‍💻 Module Components

- `client.py`: Encrypts a transaction with AES and sends it using `client_runner`.
- `attacker.py`: Forges a message, encrypts it with the same AES key, and sends it.
- `server.py`: Decrypts AES messages using `server_runner`, with no authentication.

## 🎓 Educational Purpose

This module teaches:
- Encryption ≠ authentication
- Why messages should be authenticated (e.g. with HMAC or signatures)
- The danger of assuming encrypted = secure without verifying sender identity
