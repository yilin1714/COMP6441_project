
def get_all_protocols():
    return [
        # -------- Insecure Protocols --------
        {
            "name": "Insecure - No Auth, No Encryption",
            "description": "No authentication or encryption. Everything is plaintext.",
            "vulnerability": "Completely open to spoofing and sniffing.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/1_no_auth_no_encryption",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Base64 Fake Encryption",
            "description": "Obfuscates data using Base64 but offers no real protection.",
            "vulnerability": "Trivially reversible encoding.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/2_base64_fake_encryption",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - AES, No Authentication",
            "description": "Adds AES encryption, but lacks authentication or integrity check.",
            "vulnerability": "Replay attacks, forgery still possible.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/3_no_authentication_only",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Parameter Injection",
            "description": "Client can inject unauthorized parameters into request.",
            "vulnerability": "Server fails to validate parameters properly.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/4_parameter_injection",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Fixed Session ID",
            "description": "Session ID is hardcoded or predictable.",
            "vulnerability": "Session hijacking through ID reuse.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/5_fixed_session_id",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Replay Attack (No Nonce)",
            "description": "Server does not verify message uniqueness.",
            "vulnerability": "Replay attacks possible without nonce.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/6_replay_attack_no_nonce",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Client Trust Error",
            "description": "Server trusts values like 'balance' sent by client.",
            "vulnerability": "Critical logic flaw — client can manipulate data.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/7_client_trust_error",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Insecure - Predictable Token",
            "description": "Session/token values are guessable by attacker.",
            "vulnerability": "Token brute-force possible.",
            "stage_type": "Insecure",
            "secure": False,
            "path": "protocols/insecure/8_predictable_token",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },

        # -------- Improved Protocols --------
        {
            "name": "Improved - Add Password Authentication",
            "description": "Adds password-based authentication to prevent spoofed requests.",
            "vulnerability": "Still vulnerable to sniffing (plaintext).",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - No Auth, No Encryption",
            "path": "protocols/improved/1_add_password_auth",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Use AES Instead of Base64",
            "description": "Replaces Base64 with real encryption (AES).",
            "vulnerability": "Lacks message integrity (no MAC).",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Base64 Fake Encryption",
            "path": "protocols/improved/2_aes_encryption",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Add MAC",
            "description": "Appends a message authentication code to detect tampering.",
            "vulnerability": "Still replayable without nonce.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - AES, No Authentication",
            "path": "protocols/improved/3_add_mac",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Enforce Parameter Whitelist",
            "description": "Rejects any unexpected or injected parameters in requests.",
            "vulnerability": "Prevents parameter injection via field whitelisting.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Parameter Injection",
            "path": "protocols/improved/4_whitelist_params",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Random Session ID Allocation",
            "description": "Uses a handshake to negotiate unique, unpredictable session IDs.",
            "vulnerability": "Prevents hijacking via fixed or guessable session ID.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Fixed Session ID",
            "path": "protocols/improved/5_random_session_id",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Add Nonce to Prevent Replay",
            "description": "Adds a unique nonce to each request to prevent replay attacks.",
            "vulnerability": "Requires synchronized nonce tracking.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Replay Attack (No Nonce)",
            "path": "protocols/improved/6_add_nonce",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Server-Controlled State",
            "description": "Moves all state (e.g. balance) to the server-side for verification.",
            "vulnerability": "Fixes logic flaw where client can send fake values.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Client Trust Error",
            "path": "protocols/improved/7_server_state_auth",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },
        {
            "name": "Improved - Random Signed Token with Expiry",
            "description": "Generates tokens using secure randomness and limits their validity.",
            "vulnerability": "Defends against token guessing attacks.",
            "stage_type": "Improved",
            "secure": False,
            "improves": "Insecure - Predictable Token",
            "path": "protocols/improved/8_secure_token",
            "server": "improved_server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        },

        # -------- Secure Final Protocol --------
        {
            "name": "Final - AES + Nonce + MAC",
            "description": "Combines encryption, nonce, and authentication for a secure protocol.",
            "vulnerability": "None known in current threat model.",
            "stage_type": "Secure",
            "secure": True,
            "improves": None,
            "path": "protocols/final_secure_protocol",
            "server": "server.py",
            "client": "client.py",
            "attacker": "attacker.py",
            "readme": "README.md"
        }

    ]
