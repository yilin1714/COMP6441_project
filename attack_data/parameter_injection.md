# 🔹 Parameter Injection

## 📖 Description: 
Parameter injection occurs when the client sends sensitive or privileged fields (e.g., `role=admin`, `balance=9999`) in
a request, and the server blindly trusts and applies those values without verification. This allows attackers to
escalate privileges, manipulate internal states, or forge actions.

## 🧪 Attack Scenario / Use Case: 
Consider an online banking system where the client includes a `balance` parameter in the request. If the server does not
recalculate or validate the balance, an attacker could set `balance=9999999` in their request and trick the server into
accepting it. Similarly, sending `role=admin` could escalate privileges if unchecked.

## 🔬 How It Works:

1. The attacker crafts a request with injected fields like `role=admin&balance=99999`.
2. The server accepts these fields and applies them directly to its internal logic or database.
3. As a result, the attacker can escalate privileges, alter values, or bypass security checks.

## 🛡 Mitigation:

- Never trust client-supplied values for sensitive fields.
- Validate and whitelist only allowed parameters.
- Calculate critical values like balance or roles server-side.

