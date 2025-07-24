import time

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from utils.utils import print_fixed_rule

console = Console()

THEORY = {
    "stage1": {
        "title": "Stage 1 – No Auth, No Encryption",
        "goal": "Introduce the risk of having no authentication or encryption.",
        "problem": "Messages can be read, modified, and forged in transit.",
        "mechanism": "No protection at all. Messages are sent over raw TCP in plaintext.",
        "flaws": "Replay attacks, impersonation, and tampering are all possible.",
        "suggest": "Add password authentication and encryption to secure the channel."
    },
    "stage4": {
        "title": "Stage 4 – Parameter Injection",
        "goal": "Expose the danger of trusting client-side parameters.",
        "problem": "Client can set fields like 'role=admin' or 'balance=9999', and the server accepts it.",
        "mechanism": "Server directly applies client-supplied parameters without validation.",
        "flaws": "Privilege escalation, fake balances, and business logic corruption.",
        "suggest": "Enforce parameter whitelisting and perform all critical checks server-side."
    },
    "stage5": {
        "title": "Stage 5 – Fixed Session ID",
        "goal": "Show how static session identifiers allow impersonation.",
        "problem": "A predictable or reused session ID can be guessed or replayed by attackers.",
        "mechanism": "The server accepts a static session ID passed by the client.",
        "flaws": "Attacker can hijack sessions without needing credentials.",
        "suggest": "Use randomly generated session IDs and rotate them regularly."
    },
    "stage6": {
        "title": "Stage 6 – Replay Attack (No Nonce)",
        "goal": "Prevent replay attacks using nonces.",
        "problem": "Duplicate messages can be replayed without detection.",
        "mechanism": "Client includes a nonce with each request; the server must track and reject reused values.",
        "flaws": "If the server does not track or expire nonces, replay attacks are still possible.",
        "suggest": "Use per-session nonces or timestamps with expiration tracking."
    },
    "stage8": {
        "title": "Stage 8 – Predictable Token",
        "goal": "Show how weak token generation allows session hijacking.",
        "problem": "Tokens like incremental integers or timestamps can be guessed by attackers.",
        "mechanism": "Token is issued after login, but is predictable or lacks verification.",
        "flaws": "Attacker can forge or guess tokens to access other users' sessions.",
        "suggest": "Use cryptographically secure random tokens signed with HMAC and include expiry."
    },
    "whatsapp_2019": {
        "title": "Case Study – WhatsApp Replay Attack (2019)",
        "goal": "Show that encryption alone does not prevent replay.",
        "problem": "Messages could be resent because no unique ID or nonce was used per message.",
        "mechanism": "End-to-end encryption was present, but the server couldn't detect duplicate ciphertexts.",
        "flaws": "No message ID, no sequence number, no expiry.",
        "suggest": "Use nonce, MAC, or timestamp to make each encrypted message unique."
    },
    "swift_2016": {
        "title": "Case Study – SWIFT Banking Attack (2016)",
        "goal": "Demonstrate how protocol trust violations enabled large-scale fund theft.",
        "problem": "Attackers modified SWIFT messages and bypassed business rule validations.",
        "mechanism": "SWIFT relied on formatted plain-text messages and lacked layered security.",
        "flaws": "Forged parameters, lack of verification, and weak operational controls.",
        "suggest": "Use authenticated encryption, internal approval layers, and field-level integrity checks."
    }
}


def show_theory(stage_key: str):
    if stage_key not in THEORY:
        console.print(f"[red]❌ No theory available for '{stage_key}'[/red]")
        return

    t = THEORY[stage_key]
    content = f"""
[bold]🎯 Goal:[/bold] {t['goal']}
[bold]⚠️ Problem:[/bold] {t['problem']}
[bold]🔧 Mechanism:[/bold] {t['mechanism']}
[bold]🕳️ Flaws:[/bold] {t['flaws']}
[bold]🚀 Suggested Fixes:[/bold] {t['suggest']}
"""
    console.print(Panel(content.strip(), title=f"📘 {t['title']}", border_style="cyan", width=100))


def view_protocol_theory():

    while True:
        print_fixed_rule(label="📘 Protocol Theory / Background")

        keys = list(THEORY.keys())

        print()
        for idx, key in enumerate(keys, 1):
            console.print(f"[{idx}] {THEORY[key]['title']}")
        console.print("[0] ← Back\n")

        choice = Prompt.ask("Select a stage", choices=[str(i) for i in range(1, len(keys) + 1)] + ["0"])

        if choice == "0":
            break

        idx = int(choice) - 1
        if 0 <= idx < len(keys):
            show_theory(keys[idx])

        time.sleep(0.8)