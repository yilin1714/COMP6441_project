import time

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from utils.network import find_available_port
from utils.notifier import ServerReadyListener
from utils.utils import print_fixed_rule
from utils.readme_viewer import show_readme
from utils.script_runner import run_script

console = Console()


def launch_protocol_menu(protocol: dict):
    print()
    print_fixed_rule(label=f"🚀 {protocol['name']}", text_style="bold cyan")

    server_port = find_available_port()
    notify_port = find_available_port()

    listener = ServerReadyListener(notify_port)

    console.print("[bold green][Auto][/bold green] Starting server...")
    run_script(protocol["server"], protocol["path"], label="SERVER",
               args=["--port", str(server_port), "--notify-port", str(notify_port)])

    server_message = listener.wait()

    if "[!]" in server_message or not server_message.lower().startswith("ready"):
        console.print(f"[red]❌ Server failed to start properly.[/red]")
        return

    console.print(Panel(server_message, title="Server says", border_style="cyan", width=80))

    while True:
        print()
        print_fixed_rule(label="Protocol Interaction Menu", text_style="bold cyan")

        console.print("\n[1] Run Client")
        console.print("[2] Run Attacker")
        console.print("[3] View README")
        console.print("[0] Back")

        choice = Prompt.ask("\nSelect an action", choices=["1", "2", "3", "0"])

        if choice == "1":
            run_script(protocol["client"], protocol["path"], label="CLIENT", args=["--port", str(server_port)])
            time.sleep(1.2)

        elif choice == "2":
            run_script(protocol["attacker"], protocol["path"], label="ATTACKER", args=["--port", str(server_port)])
            time.sleep(1.2)

        elif choice == "3":
            show_readme(protocol["readme"], protocol["path"])
            time.sleep(1.2)

        elif choice == "0":
            break
