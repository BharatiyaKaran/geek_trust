from sys import argv
from src.command import CommandRegistry


def process_commands(lines):
    command_registry = CommandRegistry()
    for line in lines:
        command_registry.register(line)
    command_registry.execute()


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    # process all input commands
    process_commands(Lines)


if __name__ == "__main__":
    main()
