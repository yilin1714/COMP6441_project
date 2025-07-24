from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich import box
from modes.launcher import launch_protocol_menu
from utils.protocol_config import get_all_protocols
from utils.utils import print_fixed_rule

console = Console()


def view_protocol_stages():
    all_protocols = get_all_protocols()

    stage_types = {
        "1": "Insecure",
        "2": "Improved",
        "3": "Secure",
        "4": "All",
        "0": "Back"
    }

    while True:

        print()
        print_fixed_rule(label="📂 View Protocol Stages by Category", text_style="bold cyan")

        console.print("[1] ❌ Insecure Protocols")
        console.print("[2] 🔧 Improved Protocols")
        console.print("[3] ✅ Secure Protocol")
        console.print("[4] 📋 View All")
        console.print("[0] 🔙 Back to Main Menu")

        choice = Prompt.ask("\nSelect a category", choices=list(stage_types.keys()))
        selected_type = stage_types[choice]

        if selected_type == "Back":
            break

        if selected_type == "All":
            filtered_protocols = all_protocols
        else:
            filtered_protocols = [p for p in all_protocols if p["stage_type"] == selected_type]

        if not filtered_protocols:
            console.print("[yellow]No protocols available for this category.[/yellow]")
            return

        while True:

            print()
            print_fixed_rule(label=f"{selected_type} Protocols", text_style="bold cyan")

            table = Table(show_header=True, header_style="bold magenta", box=box.SQUARE)
            table.add_column("ID", justify="center", style="cyan", no_wrap=True)
            table.add_column("Name", style="bold white")
            table.add_column("Vulnerability", style="dim")

            index_map = {}
            for idx, proto in enumerate(filtered_protocols, 1):
                table.add_row(str(idx), proto["name"], proto.get("vulnerability", "—"))
                index_map[str(idx)] = proto

            console.print(table)

            _choices = list(index_map.keys()) + ["0"]

            selection = Prompt.ask("\nSelect a protocol to launch (0 for return)", choices=_choices)

            if selection == "0":
                print("↩️  Returning to previous menu...")
                break

            selected_protocol = index_map[selection]

            launch_protocol_menu(selected_protocol)
