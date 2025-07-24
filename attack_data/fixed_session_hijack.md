# 🔹 Session Hijack via Fixed Session ID

## 📖 Description: 
In this attack, the server assigns a static or predictable session ID (e.g., `session_id = 12345`) that does not change
between users or sessions. An attacker can either guess or reuse this ID to impersonate legitimate users and gain
unauthorized access.

## 🧪 Attack Scenario / Use Case:
Suppose a web service sets a fixed session ID like `session_id=42` for all users upon login. An attacker who knows or
guesses this value can craft a request using the same ID and gain access to another user's session without needing to
authenticate.

## 🔬 How It Works:

1. The attacker observes or guesses a static session ID.
2. They use this ID to craft a malicious request (e.g., fund transfer, profile access).
3. The server validates the session based only on the ID and grants access.
4. No randomness or binding to user/device/IP allows easy impersonation.

## 🛡 Mitigation:
To prevent this attack:

- Use cryptographically secure random session tokens.
- Rotate session IDs on reauthentication.
- Optionally bind session IDs to user attributes (IP, agent fingerprint).

