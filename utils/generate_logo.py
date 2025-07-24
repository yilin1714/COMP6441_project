from pyfiglet import Figlet
from rich.text import Text
from rich.console import Console


def get_logo(text="ProtoBreak", font="slant", color=None):
    fig = Figlet(font=font)
    result = fig.renderText(text)

    if color:
        return Text(result, style=color)
    return result


if __name__ == "__main__":
    console = Console()
    console.print(get_logo(color="blue"))
