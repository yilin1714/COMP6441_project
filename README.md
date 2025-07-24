# 🔐 Secure Protocol Simulation Platform

> 🎓 An educational framework for demonstrating insecure and secure communication protocols, supporting live attacks and
> step-by-step protocol hardening.

📘 [Overview](#overview) | 🧪 [Protocol Stages](#protocol-stages) | 🚀 [Getting Started](#getting-started) | 🖥️ [Project Structure](#project-structure) | 🎓 [Educational Purpose](#educational-purpose)

---

## Overview

The **Secure Protocol Simulation Platform** is a teaching-oriented system that enables students to interact with various
stages of protocol security, from plaintext vulnerable communication to fully encrypted, authenticated, and
replay-protected systems.

It provides:

- 🧠 Protocol logic simulation
- ⚔️ Built-in attack scripts for each stage
- 🔁 Replay, tampering, and session hijacking examples
- 🧪 Real-time responses for visual feedback

---

## Protocol Stages

### Insecure Stages

| Stage | Directory                | Name/Feature            | Main Vulnerability               |
|-------|--------------------------|-------------------------|----------------------------------|
| 1     | 1_no_auth_no_encryption  | No Auth, No Encryption  | Everything is plaintext          |
| 2     | 2_base64_fake_encryption | Base64 Fake Encryption  | Obfuscation only, not encryption |
| 3     | 3_no_authentication_only | AES, No Authentication  | No auth, replay/forgery possible |
| 4     | 4_parameter_injection    | Parameter Injection     | Parameter tampering              |
| 5     | 5_fixed_session_id       | Fixed Session ID        | Session hijack                   |
| 6     | 6_replay_attack_no_nonce | No Nonce, Replay Attack | Replay attack                    |
| 7     | 7_client_trust_error     | Client Trust Error      | Client-side trust flaw           |
| 8     | 8_predictable_token      | Predictable Token       | Token/session brute-force        |

### Improved Stages

| Stage | Directory           | Name/Feature         | Main Security Improvement     |
|-------|---------------------|----------------------|-------------------------------|
| 1     | 1_add_password_auth | Add Password Auth    | Basic password authentication |
| 2     | 2_aes_encryption    | AES Encryption       | Adds encryption               |
| 3     | 3_add_mac           | Add MAC              | Message integrity (MAC)       |
| 4     | 4_whitelist_params  | Whitelist Parameters | Parameter validation          |
| 5     | 5_random_session_id | Random Session ID    | Unpredictable session IDs     |
| 6     | 6_add_nonce         | Add Nonce            | Prevents replay attacks       |
| 7     | 7_server_state_auth | Server State Auth    | Server-side session state     |
| 8     | 8_secure_token      | Secure Token         | Strong token, HMAC, expiry    |

### Secure Stage

| Directory             | Name/Feature          | Security Properties                      |
|-----------------------|-----------------------|------------------------------------------|
| final_secure_protocol | Final Secure Protocol | AES, HMAC, Nonce, Token, Full protection |

---

## Getting Started

### Installation

```bash
git clone https://github.com/yilin1714/COMP6441_project.git
cd COMP6441_project
pip install -r requirements.txt
```

> Requires Python 3.8+ and the dependencies in `requirements.txt` (`pycryptodome`, `rich`, `pyfiglet`)

### Run the Platform

Start the simulation using the unified entry point:

```bash
python3 main.py
```

You will be able to:

- Select a protocol stage (e.g., insecure / improved / secure)
- Launch the server, client, or attacker from one interface

> All default settings can also be adjusted in `config.py`.


---

## Project Structure

### 📂 Current Structure

```
COMP6441_project/
├── attack_data/             # Replay/nonces/session samples for attack simulation
├── modes/                   # UI / CLI mode handlers
├── protocols/               # All protocol versions (insecure → secure)
│   ├── insecure/
│   ├── improved/
│   └── final_secure_protocol/
├── utils/                   # Common utilities (parsers, server/client runner)
├── config.py                # Global configuration
├── main.py                  # Entry launcher for the platform
```

---

## Educational Purpose

- 🔍 Understand protocol-level flaws beyond encryption
- 💥 Simulate attacks like replay, forgery, hijacking
- 🔐 Learn layered defense with minimal code changes
- 🧩 Designed for labs, workshops, and self-study
