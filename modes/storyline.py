from utils.readme_viewer import show_readme
from utils.script_runner import run_script
from rich.prompt import Prompt, Confirm
from rich.console import Console

console = Console()

STAGES = [
    {
        "title": "Stage 1 – No Auth, No Encryption",
        "path": "insecure/1_no_auth_no_encryption",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9000"
    },
    {
        "title": "Stage 4 – Parameter Injection",
        "path": "insecure/4_parameter_injection",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9003"
    },
    {
        "title": "Stage 5 – Fixed Session ID",
        "path": "insecure/5_fixed_session_id",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9004"
    },
    {
        "title": "Stage 6 – Replay Attack (No Nonce)",
        "path": "insecure/6_replay_attack_no_nonce",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9005"
    },
    {
        "title": "Stage 8 – Predictable Token",
        "path": "insecure/8_predictable_token",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9007"
    },
    {
        "title": "Improved Stage 6 – Add Nonce",
        "path": "improved/6_add_nonce",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9005"
    },
    {
        "title": "Improved Stage 8 – Secure Token",
        "path": "improved/8_secure_token",
        "server": "server.py",
        "readme": "README.md",
        "attacker": "attacker.py",
        "port": "9007"
    }
]

def run_stage(stage):
    console.rule(f"[bold cyan]{stage['title']}")
    if Confirm.ask("📘 View README for this stage?"):
        show_readme(stage["readme"], stage["path"])

    if Confirm.ask("🖥️  Launch the server?"):
        run_script(stage["server"], stage["path"], label="SERVER")

    if Confirm.ask("💣 Run attacker against this stage?"):
        run_script(stage["attacker"], stage["path"], label="ATTACK", args=["--port", stage["port"]])

    console.print("\n✅ Stage complete.\n")

def storyline_runner():
    console.print("[bold blue]\n=== Interactive Protocol Storyline ===[/bold blue]\n")
    while True:
        for idx, stage in enumerate(STAGES, 1):
            console.print(f"[{idx}] {stage['title']}")
        console.print("[0] Exit\n")

        choice = Prompt.ask("Select a stage to explore", choices=[str(i) for i in range(0, len(STAGES)+1)])
        if choice == "0":
            console.print("👋 Exiting storyline.")
            break

        idx = int(choice) - 1
        if 0 <= idx < len(STAGES):
            run_stage(STAGES[idx])

if __name__ == "__main__":
    storyline_runner()