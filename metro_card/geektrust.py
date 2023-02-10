from sys import argv
from src.services import CommandService


def process_commands(lines):
    command_service = CommandService()
    command_service.register(lines)
    command_service.execute()


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
