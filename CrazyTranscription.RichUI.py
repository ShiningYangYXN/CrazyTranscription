# -*- coding: utf-8 -*-

# Dependencies

from rich.console import Console
from rich.markup import escape

from CrazyTranscription import *

# Define the console

console = Console()

# Mainloop: Rich Interface

console.print("Welcome to CrazyTranscription!", style="bold blue", justify="center")
console.print(
    "Version [blue bold]2.2.1.2 (Arctic Wolf)[/blue bold], made with [red bold]love[/red bold] by [link=https://github.com/ShiningYangYXN]Shining Yang[/link]"
)
console.print(
    "Visit [link=https://github.com/ShiningYangYXN/CrazyTranscription]https://github.com/ShiningYangYXN/CrazyTranscription[/link] for project updates."
)
while True:
    mode = ""
    console.print("Please select a mode:", style="blue")
    console.print("    [bold]\\[1][/bold] Transcription", style="green")
    console.print("    [bold]\\[2][/bold] Reverse Transcription", style="yellow")
    console.print("    [bold]\\[#][/bold] Exit", style="red")
    mode = console.input("[blue bold]Mode: [/blue bold]")
    if mode == "1":
        mode = ""
        modeNames = {
            "1": "Greek",
            "2": "Cyrillic",
            "3": "Arabic",
            "4": "Hebrew",
            "5": "Sanskrit",
            "6": "Tibetan",
        }
        while mode != "#":
            console.print("Transcription mode. Please select a target:", style="blue")
            console.print("    [bold]\\[1][/bold] Latin to Greek", style="blue")
            console.print("    [bold]\\[2][/bold] Latin to Cyrillic", style="blue")
            console.print("    [bold]\\[3][/bold] Latin to Arabic", style="blue")
            console.print("    [bold]\\[4][/bold] Latin to Hebrew", style="blue")
            console.print("    [bold]\\[5][/bold] Latin to Sanskrit", style="blue")
            console.print("    [bold]\\[6][/bold] Latin to Tibetan", style="blue")
            console.print("    [bold]\\[#][/bold] Exit", style="red")
            mode = console.input("[blue bold]Mode: [/blue bold]")
            if mode in ["1", "2", "3", "4", "5", "6"]:
                selectedTranscriber = DefaultTranscribers[int(mode) - 1]
                text = ""
                console.print(
                    f"[blue bold]Latin to {modeNames[mode]}[/blue bold] Mode [green]selected[/green]. [red bold]Type '#' to exit.[/red bold]"
                )
                while text != "#":
                    text = console.input(
                        "[blue bold]Input your text to be transcribed:\n[/blue bold]"
                    )
                    console.rule(f"BEGIN {modeNames[mode].upper()} TRANSCRIPTION")
                    console.print(escape(selectedTranscriber.Transcribe(text)))
                    console.rule(f"END {modeNames[mode].upper()} TRANSCRIPTION")
                console.print("OK,thanks. Goodbye.", style="blue bold")
            elif mode == "#":
                console.print("OK,thanks. Goodbye.", style="blue bold")
                pass
            else:
                console.print("Invalid input. Please try again.", style="red bold")

    elif mode == "2":
        console.print(
            "[blue bold]Reverse Transcription Mode.[/blue bold] [red bold]Type '#' to exit.[/red bold]"
        )
        text = ""
        while text != "#":
            text = console.input(
                "[blue bold]Input your text to be transcribed:\n[/blue bold]"
            )
            console.rule("BEGIN REVERSE TRANSCRIPTION")
            for t in DefaultTranscribers:
                text = t.ReverseTranscribe(text)
                console.print(escape(text))
                console.rule("END REVERSE TRANSCRIPTION")
        console.print("OK,thanks. Goodbye.", style="blue bold")
    elif mode == "#":
        console.print("OK,thanks. Goodbye.", style="blue bold")
        break
    else:
        console.print("Invalid input. Please try again.", style="red bold")
