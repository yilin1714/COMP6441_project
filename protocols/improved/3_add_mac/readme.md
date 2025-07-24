# 🔐 Plaintext + MAC (Stage 3 - Message Integrity without Encryption)

This module replaces encryption with integrity protection using **HMAC-SHA256**.
It demonstrates how even in unencrypted protocols, message tampering can be detected reliably.

---

## 📘 Overview

In this stage:
- The **client** constructs a plaintext message and appends an HMAC-SHA256 value.
- The **server** verifies the HMAC to confirm the message was not altered in transit.
- The **attacker** tries to:
  - Omit the MAC
  - Forge an incorrect MAC
  - Reuse a valid MAC with a tampered message

---

## ✅ Improvements Introduced

- **✅ HMAC-SHA256** ensures message integrity even over plaintext.
- **✅ Server rejects malformed or tampered messages.**

---

## ⚠️ Remaining Vulnerabilities

- ❌ No confidentiality: messages are readable by anyone on the network.
- ❌ No user identity/authentication.
- ❌ No replay protection (no nonce or timestamp).

---

## 🎯 Message Format

Before transmission:
```
username=alice&action=transfer&amount=1000
```

After HMAC is appended:
```
username=alice&action=transfer&amount=1000&mac=<hmac-sha256>
```

This full message is sent in **plaintext**.

---

## 🧪 Example (Valid Client Request)

```
username=alice&action=transfer&amount=1000&mac=3f4a1d8f9a2e...
```

Server response:
```
✅ Verified. Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 💥 Example (Attacker Request)

- **Missing MAC**:
  ```
  [!] MAC missing.
  ```

- **Invalid MAC**:
  ```
  [!] MAC verification failed.
  ```

- **Tampered message with reused MAC**:
  ```
  [!] MAC verification failed.
  ```

---

## 🧑‍💻 Module Components

- `client.py`: Builds message, computes and appends MAC, sends plaintext.
- `improved_server.py`: Receives plaintext, validates MAC.
- `attacker.py`: Sends forged, incomplete, or tampered messages.

---

## 🎓 Educational Purpose

This module teaches:
- That message integrity is a separate concern from confidentiality
- How HMAC protects data from modification
- That encryption is not required to detect tampering

---
