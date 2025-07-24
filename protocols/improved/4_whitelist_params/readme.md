# 🧱 Plaintext + Whitelist (Stage 4 - Parameter Filtering)

This module demonstrates how a protocol can restrict incoming data by enforcing a **parameter whitelist**. 
No encryption or integrity mechanisms are used; instead, the server simply validates that only allowed fields are present in the request.

---

## 📘 Overview

In this stage:
- The **client** sends a plaintext transaction message.
- The **server** receives the message and enforces a **whitelist** of allowed keys.
- The **attacker** attempts to inject unauthorized fields like `is_admin=true`.

---

## ✅ Improvements Introduced

- ✅ Whitelist enforcement blocks unexpected parameters.
- ✅ Simple protection against parameter injection.
- ✅ No encryption or MAC required.

---

## ⚠️ Remaining Vulnerabilities

- ❌ No encryption: messages are readable in transit.
- ❌ No integrity check: messages can be modified.
- ❌ No authentication or replay protection.

---

## 🎯 Allowed Fields

The server only accepts the following keys:
```
username, action, amount, mac
```

Any additional fields will result in rejection.

---

## 🧪 Example (Valid Request)

```
username=alice&action=transfer&amount=1000
```

✅ Server responds:
```
✅ Validated. Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 💥 Example (Attacker Request)

```
username=alice&action=transfer&amount=1000&is_admin=true
```

❌ Server responds:
```
[!] Request contains unexpected or forbidden parameters.
```

---

## 🧑‍💻 Module Components

- `client.py`: Sends valid whitelisted transaction in plaintext.
- `improved_server.py`: Receives plaintext, enforces field whitelist.
- `attacker.py`: Sends plaintext with unauthorized fields to trigger rejection.

---

## 🎓 Educational Purpose

This module demonstrates:
- That even without encryption or MAC, semantic validation is essential
- How servers must control **what data** clients are allowed to send
- Why **whitelisting** is preferred over blacklisting in protocol design

---