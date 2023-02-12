from src.command.add_subscription import AddSubscription
from src.command.add_topup import AddTopUp
from src.command.print_renew_details import PrintRenewDetails
from src.command.start_subscription import StartSubscription


class CommandRegistry:
    def __init__(self):
        self.commands = []

    def register(self, input: str):
        cmd_str = input.rstrip("\n").split(" ")
        if cmd_str[0] == 'START_SUBSCRIPTION':
            command = StartSubscription(cmd_str[1])
        elif cmd_str[0] == 'ADD_SUBSCRIPTION':
            command = AddSubscription(cmd_str[1], cmd_str[2])
        elif cmd_str[0] == 'ADD_TOPUP':
            command = AddTopUp(cmd_str[1], cmd_str[2])
        elif cmd_str[0] == 'PRINT_RENEWAL_DETAILS':
            command = PrintRenewDetails()
        else:
            return

        self.commands.append(command)

    def unregister(self, command):
        self.commands.remove(command)

    def execute(self):
        for command in self.commands:
            command.execute()
