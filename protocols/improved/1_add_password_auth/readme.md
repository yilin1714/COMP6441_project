# 🛡️ Add Password Authentication

This module improves upon the fully insecure protocol by introducing **basic password-based authentication**.  
It serves as the first step toward designing a more secure protocol and demonstrates the value (and limitations) of shared-secret authentication.

## 📘 Overview

In this demo:
- The **client** sends a request including a hardcoded password.
- The **server** verifies the password before processing the transaction.
- The **attacker** can attempt to replay or guess the password, but will fail if the password is incorrect.

## 🔐 Improvements Introduced

- **✅ Basic Authentication**: Only clients that include the correct password can issue a valid request.
- **❌ Still No Encryption**: All credentials and data are still visible to eavesdroppers.
- **❌ No Integrity Check**: Messages can still be altered in transit.

## 🎯 Message Format

Requests follow the form:
```
username=<name>&action=<action>&amount=<value>&password=<secret>
```

The server accepts the operation **only if** the provided password matches the expected one.

## 🧪 Example (Authenticated Client)

```
username=alice&action=transfer&amount=1000&password=cybersecurity
```

Server responds:
```
✅ Authenticated. Action 'transfer' by 'alice' with amount $1000 accepted.
```

## 💥 Example (Failed Authentication)

```
username=alice&action=transfer&amount=1000&password=hacker
```

Server responds:
```
[!] Authentication failed: invalid or missing password.
```

## 🧑‍💻 Module Components

- `client.py`: Sends a transaction request including a shared password.
- `attacker.py`: Attempts to spoof a request with an incorrect or missing password.
- `improved_server.py`: Verifies the password and rejects unauthenticated requests.

## 🎓 Educational Purpose

This example illustrates:
- How **basic authentication** improves protocol security
- Why **encryption** is still needed even with authentication
- That **hardcoded passwords** are not a long-term security solution
