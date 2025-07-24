# 🤝 Client Trust Error (Logic Flaw)

This module demonstrates a flawed protocol in which the server blindly trusts client-provided input for sensitive values like account balance. This introduces serious security risks, as attackers can manipulate their own balance claims and bypass server-side logic.

## 📘 Overview

In this demo:
- The **client** sends a transaction request including a `balance` field that reflects the user's account.
- The **server** accepts and trusts the `balance` field as-is, without verifying it against a secure backend.
- The **attacker** modifies this value to falsely claim a much higher balance and trick the server into approving a large withdrawal.

## 🔐 Vulnerabilities Demonstrated

- **Blind Trust in Client Input**: Server trusts `balance=...` from the client without server-side verification.
- **No Input Validation**: Malicious values (e.g. inflated balance) are accepted at face value.
- **No Authorization or Access Control**: The server does not cross-check whether the action should be allowed based on account rules.

## 🎯 Message Format

The messages follow this format:
```
username=<user>&balance=<claimed_balance>&action=<operation>
```

## 🧪 Example (Benign Client)

Request:
```
username=alice&balance=100&action=withdraw
```

Response:
```
✅ alice requested 'withdraw' with claimed balance $100. Accepted!
```

## 💥 Example (Attacker Exploit)

Forged request:
```
username=alice&balance=999999&action=withdraw
```

Response:
```
✅ alice requested 'withdraw' with claimed balance $999999. Accepted!
```

## 🧑‍💻 Module Components

- `client.py`: Simulates a correct user submitting accurate balance data using `client_runner`.
- `attacker.py`: Fakes a large balance using `attacker_runner` to trick the server.
- `server.py`: Uses `server_runner` to parse and trust unverified request fields.

## 🎓 Educational Purpose

This module teaches:
- Why client input must never be trusted blindly
- The importance of server-side validation and access control
- How simple logic flaws can lead to major authorization bypasses