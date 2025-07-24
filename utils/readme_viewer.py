import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def clean_and_indent_code_blocks(lines):
    in_code_block = False
    result = []

    for line in lines:
        stripped = line.rstrip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        elif in_code_block:
            result.append("    " + stripped)
        else:
            result.append(stripped)

    return result


def show_readme(readme_name: str, readme_path: str):
    readme_name = readme_name.lower()
    full_readme_path = os.path.join(readme_path, readme_name)

    if not os.path.exists(full_readme_path):
        console.print(f"[yellow]⚠️ README.md not found in {readme_path}[/yellow]")
        return

    with open(full_readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = clean_and_indent_code_blocks(lines)

    processed_lines = []
    prev_line_was_blank = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        is_header = stripped.startswith("#")

        if stripped == "":
            next_non_blank = next((l.strip() for l in lines[i + 1:] if l.strip()), None)
            if next_non_blank and next_non_blank.startswith("#"):
                processed_lines.append("")
                prev_line_was_blank = True
            else:
                continue
        else:
            if is_header and not prev_line_was_blank and processed_lines:
                processed_lines.append("")
            processed_lines.append(line.rstrip())
            prev_line_was_blank = False

    compact_content = "\n".join(processed_lines)
    console.print(Panel(Text(compact_content), title="📘 Protocol README", border_style="green", width=100))
