
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
        # console.print("[4] Restart Server")
        console.print("[4] Back")

        choice = Prompt.ask("\nSelect an action", choices=["1", "2", "3", "4"])

        if choice == "1":
            run_script(protocol["client"], protocol["path"], label="CLIENT", args=["--port", str(server_port)])
            time.sleep(1.2)

        elif choice == "2":
            run_script(protocol["attacker"], protocol["path"], label="ATTACKER", args=["--port", str(server_port)])
            time.sleep(1.2)

        elif choice == "3":
            show_readme(protocol["readme"], protocol["path"])
            time.sleep(1.2)

        elif choice == "4":
            break


# def run_script(script_name: str, script_path: str, label="PROCESS", args=None):
#     full_script_path = os.path.abspath(os.path.join(script_path, script_name))
#
#     if not os.path.exists(full_script_path):
#         console.print(f"[bold red]❌ {label} script not found: {script_path}[/bold red]")
#         return
#
#     if label == "RESTART":
#         console.print(f"[bold green]▶ Restarting SERVER...[/bold green]")
#     else:
#         console.print(f"[bold green]▶ Launching {label}...[/bold green]")
#
#     def find_project_root(path):
#         current = os.path.abspath(os.path.dirname(path))
#         while current != os.path.dirname(current):
#             if os.path.exists(os.path.join(current, "main.py")) or os.path.exists(os.path.join(current, "config.py")):
#                 return current
#             current = os.path.dirname(current)
#         return os.path.dirname(path)
#
#     project_root = find_project_root(full_script_path)
#
#     try:
#         command = ["python3", full_script_path]
#
#         if args:
#             command += args
#
#         env = os.environ.copy()
#         env["PYTHONPATH"] = project_root
#
#         if label == "RESTART" or label == "SERVER":
#             subprocess.Popen(command, cwd=project_root, env=env)
#         else:
#             subprocess.run(command, cwd=project_root, env=env)
#
#     except Exception as e:
#         console.print(f"[red]Error running {label}: {e}[/red]")


# def clean_and_indent_code_blocks(lines):
#     """
#     Process a list of text lines to remove markdown code block delimiters and indent code lines.
#
#     This function identifies markdown code blocks demarcated by triple backticks (```) and removes
#     those delimiters. It also indents every line inside a code block by four spaces to improve
#     readability when rendered in the console.
#
#     Parameters:
#         lines (List[str]): The list of lines read from a markdown file, typically README.md.
#
#     Returns:
#         List[str]: A new list of lines with code block markers removed and code lines indented.
#     """
#     in_code_block = False
#     result = []
#
#     for line in lines:
#         stripped = line.rstrip()
#
#         if stripped.startswith("```"):
#             in_code_block = not in_code_block
#             continue
#         elif in_code_block:
#             result.append("    " + stripped)
#         else:
#             result.append(stripped)
#
#     return result
#
#
# def show_readme(readme_name: str, readme_path: str):
#     readme_name = readme_name.lower()
#     full_readme_path = os.path.join(readme_path, readme_name)
#
#     if not os.path.exists(full_readme_path):
#         console.print(f"[yellow]⚠️ README.md not found in {readme_path}[/yellow]")
#         return
#
#     with open(full_readme_path, "r", encoding="utf-8") as f:
#         lines = f.readlines()
#
#     lines = clean_and_indent_code_blocks(lines)
#
#     processed_lines = []
#     prev_line_was_blank = False
#
#     for i, line in enumerate(lines):
#         stripped = line.strip()
#         is_header = stripped.startswith("#")
#
#         if stripped == "":
#             next_non_blank = next((l.strip() for l in lines[i + 1:] if l.strip()), None)
#             if next_non_blank and next_non_blank.startswith("#"):
#                 processed_lines.append("")
#                 prev_line_was_blank = True
#             else:
#                 continue
#         else:
#             if is_header and not prev_line_was_blank and processed_lines:
#                 processed_lines.append("")
#             processed_lines.append(line.rstrip())
#             prev_line_was_blank = False
#
#     compact_content = "\n".join(processed_lines)
#     console.print(Panel(Text(compact_content), title="📘 Protocol README", border_style="green", width=100))
