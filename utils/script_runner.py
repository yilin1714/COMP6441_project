import os
import subprocess
from rich.console import Console

console = Console()


def run_script(script_name: str, script_path: str, label="PROCESS", args=None):
    full_script_path = os.path.abspath(os.path.join(script_path, script_name))

    if not os.path.exists(full_script_path):
        console.print(f"[bold red]❌ {label} script not found: {script_path}[/bold red]")
        return

    if label == "RESTART":
        console.print(f"[bold green]▶ Restarting SERVER...[/bold green]")
    else:
        console.print(f"[bold green]▶ Launching {label}...[/bold green]")

    def find_project_root(path):
        current = os.path.abspath(os.path.dirname(path))
        while current != os.path.dirname(current):
            if os.path.exists(os.path.join(current, "main.py")) or os.path.exists(os.path.join(current, "config.py")):
                return current
            current = os.path.dirname(current)
        return os.path.dirname(path)

    project_root = find_project_root(full_script_path)

    try:
        command = ["python3", full_script_path]

        if args:
            command += args

        env = os.environ.copy()
        env["PYTHONPATH"] = project_root

        if label in {"RESTART", "SERVER"}:
            subprocess.Popen(command, cwd=project_root, env=env)
        else:
            subprocess.run(command, cwd=project_root, env=env)

    except Exception as e:
        console.print(f"[red]Error running {label}: {e}[/red]")