# 🔹 Predictable Token Attack

## 📖 Description:
A predictable token attack exploits session or authentication tokens that are generated using weak or predictable
patterns (e.g., incremental integers, timestamps). If an attacker can guess a valid token, they can impersonate a
legitimate user without knowing their credentials.

## 🧪 Attack Scenario / Use Case:
Imagine a web API that issues tokens like `token_1001`, `token_1002`, etc. If an attacker sees a valid token or knows
the pattern, they can guess future or nearby tokens to hijack sessions or access protected resources without
authorization.

## 🔬 How It Works:

1. The attacker observes or guesses a valid token (e.g., `session_id=123456`).
2. They craft a request using the guessed token.
3. If the server accepts the token without additional validation (e.g., HMAC, expiration, IP binding), the attacker
   gains access.
4. This type of flaw is common in systems using poor random number generators or incremental IDs.

## 🛡 Mitigation:
To defend against predictable token attacks:

- Use cryptographically secure random token generators.
- Sign tokens with HMAC to prevent tampering.
- Include expiration timestamps and validate on the server.
