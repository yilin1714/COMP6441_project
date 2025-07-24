from rich.console import Console
from rich.text import Text


def print_fixed_rule(label: str, width: int = 100, char: str = "─", line_style: str = "dim",
                     text_style: str = "bold cyan"):
    console = Console()

    text = f" {label} "
    left = (width - len(text)) // 2
    right = width - len(text) - left

    # Build the full Text object with styled segments
    rule = Text()
    rule.append(char * left, style=line_style)
    rule.append(text, style=text_style)
    rule.append(char * right, style=line_style)

    console.print(rule)
