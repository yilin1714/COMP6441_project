# 🔁 Replay Attack with Nonce

This module demonstrates a protocol that attempts to prevent replay attacks using a `nonce` value in a plaintext
communication model. The server tracks seen nonces and rejects requests that reuse them.

---

## 📘 Overview

In this demo:

- The **client** sends a plaintext request that includes a randomly generated `nonce`.
- The **server** parses the message, checks the `nonce`, and accepts or rejects the request.
- The **attacker** replays a previously captured message with the same nonce multiple times.
- The server detects the reuse and blocks duplicate actions.

---

## 🔐 Vulnerabilities Demonstrated

- **No Encryption**: Requests are visible and modifiable in transit.
- **No Authentication**: Any client can submit a valid-looking message.
- **No Message Integrity**: No protection against tampering.
- **Replay Protection via Nonce Only**: Still lacks cryptographic verification.

---

## 🎯 Message Format

Requests follow the form:

```
username=<name>&action=<action>&amount=<value>&nonce=<unique>
```

The server checks that the nonce has not been seen before.

---

## 🧪 Example (Benign Client)

```
username=alice&action=transfer&amount=1000&nonce=fresh123
```

Server responds:

```
✅ Action 'transfer' by 'alice' with amount $1000 accepted.
```

---

## 💥 Example (Attacker Exploit)

```
username=alice&action=transfer&amount=1000&nonce=fresh123
```

Server responds:

```
❌ Replay detected. Nonce 'fresh123' has already been used.
```

---

## 🧑‍💻 Module Components

- `client.py`: Sends a request with a random nonce using `client_runner`.
- `attacker.py`: Replays a previously captured message with the same nonce.
- `server.py`: Accepts requests, tracks used nonces, and rejects duplicates.

---

## 🎓 Educational Purpose

This module demonstrates the importance of preventing replay attacks using freshness mechanisms like nonces.
It also highlights how relying solely on nonces—without encryption or authentication—leaves the system vulnerable.