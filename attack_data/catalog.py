# attack_data/catalog.py

"""
📚 Attack Catalog
Includes both insecure and flawed improved protocols.
Used by explore_by_attack.py to display attackable stages and corresponding metadata.
"""

ATTACKS = {

    "replay_attack": {
        "title": "Replay Attack",
        "affected_stage": "insecure/6_replay_attack_no_nonce",
        "script_path": "protocols/insecure/6_replay_attack_no_nonce",
        "script_name": "attacker.py",
        "readme_path": "attack_data",
        "readme_name": "replay_attack.md"
    },

    "predictable_token": {
        "title": "Predictable Token Attack",
        "affected_stage": "insecure/8_predictable_token",
        "script_path": "protocols/insecure/8_predictable_token",
        "script_name": "attacker.py",
        "readme_path": "attack_data",
        "readme_name": "predictable_token.md"
    },

    "fixed_session_hijack": {
        "title": "Session Hijack via Fixed ID",
        "affected_stage": "insecure/5_fixed_session_id",
        "script_path": "protocols/insecure/5_fixed_session_id",
        "script_name": "attacker.py",
        "readme_path": "attack_data",
        "readme_name": "fixed_session_hijack.md"
    },

    "parameter_injection": {
        "title": "Parameter Injection",
        "affected_stage": "insecure/4_parameter_injection",
        "script_path": "protocols/insecure/4_parameter_injection",
        "script_name": "attacker.py",
        "readme_path": "attack_data",
        "readme_name": "parameter_injection.md"
    }

}
