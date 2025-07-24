
from rich.markdown import Markdown
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt
from rich.text import Text
from rich import box
from rich.align import Align
import sys

from utils.generate_logo import get_logo
from utils.utils import print_fixed_rule

console = Console()


def print_welcome():
    logo = get_logo()
    if isinstance(logo, str):
        logo = Text(logo, no_wrap=True)

    console.print(Panel(Align.center(logo), style="bold cyan", box=box.ROUNDED, width=100))

    console.print(Panel(
        Align.center(
            "[bold green]Welcome to ProtoBreak[/bold green]\n[cyan]An Interactive Security Protocol Lab[/cyan]"),
        style="green",
        box=box.ROUNDED,
        width=100
    ))

    description = """
    🧪 What is ProtoBreak?
    ProtoBreak is a sandbox lab for exploring insecure protocol designs,
    demonstrating real-world attacks, and applying security improvements.

    🧭 What can you do here?
    • Walk through insecure-to-secure protocol evolution
    • Launch interactive experiments (Server / Client / Attacker)
    • Learn about replay attacks, fake tokens, missing auth, and more
    • Understand not just encryption but protocol logic flaws

    👨‍💻 For:
    Students, researchers, or anyone curious about how protocols break—and how to fix them.

    ➡️ Use the menu below to begin.
    """
    console.print(Panel(Markdown(description), box=box.DOUBLE, style="bold", width=100))


def show_main_menu():
    print()
    print_fixed_rule(label="Main Menu", line_style="bold cyan", text_style="bold green")

    menu = Text()
    menu.append("Select an option to explore:\n\n", style="bold underline")
    menu.append(" [1] View Protocol Stages\n")
    menu.append(" [2] Explore by Attack Type\n")
    menu.append(" [0] Quit")

    console.print(menu)


def handle_selection(selection: int):
    if selection == 1:
        from modes.view_protocols import view_protocol_stages
        view_protocol_stages()

    elif selection == 2:
        from modes.explore_attacks import explore_by_attack
        explore_by_attack()


    elif selection == 0:
        console.print("\n[bold red]❌ Goodbye![/bold red] 🛑 Exiting Secure Protocol Lab.\n")
        sys.exit(0)

    else:
        console.print("[bold red]Invalid selection.[/bold red] Please choose a valid option [1-3].")


def main():
    print_welcome()

    while True:
        show_main_menu()
        try:
            selection = IntPrompt.ask("\nEnter your choice", choices=["1", "2", "0"])
            handle_selection(int(selection))
        except KeyboardInterrupt:
            console.print("\n[red]Interrupted by user. Exiting.[/red]")
            break


if __name__ == "__main__":
    main()
