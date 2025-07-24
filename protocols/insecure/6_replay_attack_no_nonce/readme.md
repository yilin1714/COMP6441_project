# 🔁 Replay Attack (No Nonce, Plaintext)

This module demonstrates a protocol vulnerable to replay attacks due to the complete absence of nonce, timestamp, session tracking, or encryption. Once a valid plaintext message is observed, it can be replayed multiple times with identical results.

---

## 📘 Overview

In this demo:
- The **client** sends a plaintext transaction request.
- The **server** parses and processes the request without verifying uniqueness.
- The **attacker** simply replays the exact same message multiple times.
- The server repeats the same action every time.

---

## 🔐 Vulnerabilities Demonstrated

- **No Replay Protection**: Identical messages are accepted repeatedly.
- **No Nonce or Timestamp**: No freshness or uniqueness check.
- **No Authentication**: Any sender can issue a valid-looking command.
- **No Encryption**: Requests are visible and modifiable in transit.

---

## 🎯 Message Format

Plaintext format:
```
username=<name>&action=<action>&amount=<value>
```

This string is transmitted directly over TCP as UTF-8 text.

---

## 🧪 Example (Benign Client)

Plaintext sent:
```
username=alice&action=transfer&amount=1000
```

Server responds:
```
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 💥 Example (Attacker Replay)

Attacker replays the same plaintext message 3 times:
```
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 🧑‍💻 Module Components

- `client.py`: Sends a plaintext request using `client_runner`.
- `attacker.py`: Replays the same request multiple times using `attacker_runner`.
- `server.py`: Parses and executes requests without validation using `server_runner`.

---

## 🎓 Educational Purpose

This module teaches:
- Why protocols must include replay protection even in plaintext communication
- The importance of freshness validation (nonce, timestamp, session)
- That unencrypted channels leave systems vulnerable to both passive and active attacks
