

# 🔐 AES Encryption (Improved Stage 2)

This module replaces insecure Base64 encoding with real symmetric encryption using AES (Advanced Encryption Standard).
It demonstrates how encrypting data improves confidentiality, while also highlighting the limitations of using encryption without authentication or integrity checks.

## 📘 Overview

In this demo:
- The **client** encrypts a transaction message using AES and sends it to the server.
- The **server** decrypts the message and processes the request.
- The **attacker** attempts to break the system by sending plaintext or random Base64 strings.

## ✅ Improvements Introduced

- **✅ Real Encryption (AES-128)**: Protects data from being easily read during transmission.
- **✅ Replaces reversible Base64 encoding** from the insecure version.
- **⚠️ No Integrity or Authentication**: Anyone with the key can craft messages.

## ⚠️ Remaining Vulnerabilities

- ❌ Still uses AES in ECB mode (not semantically secure).
- ❌ No message integrity check (MAC or HMAC).
- ❌ No identity/authentication verification.
- ❌ Susceptible to replay and cut-and-paste attacks.

## 🎯 Message Format (Before Encryption)

```
username=alice&action=transfer&amount=1000
```

This message is AES-encrypted (padded to 16 bytes) and Base64-encoded before being sent.

## 🧪 Example (Valid Client Request)

Encrypted and Base64-encoded payload like:

```
Nm+OCVAYyDoR3R5zNAC3evGcCqQvMHknDKhZCG9OUQE=
```

Server responds:

```
🔐 Decrypted. Action 'transfer' by 'alice' with amount $1000 accepted.
```

## 💥 Example (Attacker Request)

Sending unencrypted or invalid hex-encoded data like:

```
username=hacker&action=steal&amount=999999
```

Or:

```
zz11ffaa8899
```

Server responds:

```
[!] Decryption failed or message is corrupted.
```

## 🧑‍💻 Module Components

- `client.py`: Encrypts and sends transaction using AES-128.
- `improved_server.py`: Decrypts request and accepts only if decryption succeeds.
- `attacker.py`: Sends malformed or forged data to test server robustness.

## 🎓 Educational Purpose

This module highlights:
- Why encryption must be paired with integrity checks.
- How lack of authentication exposes systems to spoofing.
- Why AES-ECB is not secure for real protocols.
