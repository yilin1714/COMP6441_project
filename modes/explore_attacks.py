import time

from rich.prompt import IntPrompt
from rich.console import Console
from rich.panel import Panel
from attack_data.catalog import ATTACKS

from utils.readme_viewer import show_readme
from utils.script_runner import run_script
from utils.network import find_available_port
from utils.notifier import ServerReadyListener

console = Console()


def explore_by_attack():
    while True:
        print("\n=== 🧨 Explore by Attack Type ===\n")

        attack_keys = list(ATTACKS.keys())

        for idx, key in enumerate(attack_keys, 1):
            print(f" [{idx}] {ATTACKS[key]['title']}")

        print(" [0] ← Back to Main Menu")

        # Ask for attack selection
        max_choice = len(attack_keys)
        choices = [str(i) for i in range(1, max_choice + 1)] + ["0"]

        try:
            choice = IntPrompt.ask("\nEnter the attack number", choices=choices)
        except Exception:
            print("❌ Invalid input. Please enter a number from the list.")
            continue

        if choice == 0:
            print(" ↩️ Returning to main menu...")
            return

        attack_key = attack_keys[choice - 1]
        attack_details = ATTACKS[attack_key]

        show_readme(readme_name=attack_details["readme_name"], readme_path=attack_details["readme_path"])

        # Confirm execution
        run = input("Do you want to run this attack? (y/n): ").strip().lower()

        if run == "y":
            server_port = find_available_port()
            notify_port = find_available_port()

            listener = ServerReadyListener(notify_port)

            run_script("server.py", attack_details["script_path"], label="SERVER",
                       args=["--port", str(server_port), "--notify-port", str(notify_port)])

            server_message = listener.wait()

            if "[!]" in server_message or not server_message.lower().startswith("ready"):
                console.print(f"[red]❌ Server failed to start properly.[/red]")
                return

            console.print(Panel(server_message, title="Server says", border_style="cyan", width=80))
            time.sleep(0.8)

            run_script(attack_details["script_name"], attack_details["script_path"], label="ATTACKER",
                       args=["--port", str(server_port)])

        elif run == "n":
            print("❎ Attack skipped. Returning to attack list...\n")
        else:
            print("❌ Invalid input. Returning to attack list...\n")
