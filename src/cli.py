from typing import Self
import cmd
import shlex
import time

from graph_maker import GraphMaker

class CLI(cmd.Cmd):
    intro = (
        "\n"
        "Welcome to MyApp interactive shell!\n"
        "Type 'help' to see available commands.\n"
        "Type 'quit' or 'exit' to leave the shell.\n"
    )
    prompt = "> "

    def do_simulate(self: Self, arg: str) -> None:
        """
        Creates a graph simulation of people choosing someone else to stand behind on a party.
        The graph is later represented as an interactive HTML file and opened in the default browser.
    
        Usage: simulate <n>
        <n> must be an integer greater than or equal to 2.

        Prints an error message if input is invalid.
        """
        n: int
        gm: GraphMaker

        def _is_valid_arg() -> bool:
            args: list[str]
            n: int

            try:
                args = shlex.split(arg)
                if len(args) != 1:
                    raise ValueError
                n = int(args[0])
                if n < 2:
                    raise ValueError
            except ValueError:
                print("\nUsage: simulate <times> — times must be an integer >= 2\n")
                return False
            return True
        
        if not _is_valid_arg(): return
        
        n = int(shlex.split(arg)[0])
        gm = GraphMaker(n)
        gm.show()
        gm.clear()

        return
    
    def do_quit(self: Self, arg: str) -> bool:
        """Exit the shell."""
        print("\nSee you next time!\n")
        return True

    def do_exit(self: Self, arg: str) -> bool:
        """Exit the shell."""
        return self.do_quit(arg)
    
    def emptyline(self) -> bool:
        """Do nothing on empty input (prevents repeating last command)."""
        return True

    def default(self: Self, line: str) -> None:
        print(f"\nUnknown command: {line!r}. Type 'help' for a list of commands.\n")
        return
    
    def do_help(self: Self, arg: str):
        """Show general help or command-specific help."""
        if arg: return super().do_help(arg) # Use default cmd behavior for command-specific help
        
        print(
            "\nCommands:\n"
            "  simulate <n>       Simulate the 'simulate' command (n >= 2)\n"
            "  help               Show this message\n"
            "  quit / exit        Exit the shell\n"
            "\nType 'help <command>' for command-specific help\n"
        )
