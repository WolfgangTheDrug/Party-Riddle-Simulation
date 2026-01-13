from cli import CLI

def main() -> None:
    cli: CLI

    cli = CLI()
    cli.cmdloop()

if __name__ == '__main__':
    main()
