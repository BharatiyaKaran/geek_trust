# File to register all commands

from .balance_command import BalanceCommand
from .checkin_command import CheckInCommand
from .print_command import PrintCommand


class CommandRegistry:
    def __init__(self):
        self.commands = []

    def register(self, input: str):
        cmd_str = input.rstrip("\n").split(" ")
        if cmd_str[0] == 'BALANCE':
            command = BalanceCommand(cmd_str[1], cmd_str[2])
        elif cmd_str[0] == 'CHECK_IN':
            command = CheckInCommand(cmd_str[1], cmd_str[2], cmd_str[3])
        elif cmd_str[0] == 'PRINT_SUMMARY':
            command = PrintCommand()

        else:
            # print("Invalid command, skipping ...")
            return

        self.commands.append(command)

    def unregister(self, command):
        self.commands.remove(command)

    def execute(self):
        for command in self.commands:
            command.execute()
