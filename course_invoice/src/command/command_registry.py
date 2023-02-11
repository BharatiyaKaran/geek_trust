from src.command.add_pro_member import AddProMember
from src.command.add_program import AddProgram
from src.command.apply_coupon import ApplyCoupon
from src.command.print_bill import PrintBill


class CommandRegistry:
    def __init__(self):
        self.commands = []

    def register(self, input: str):
        cmd_str = input.rstrip("\n").split(" ")
        if cmd_str[0] == 'ADD_PROGRAMME':
            command = AddProgram(cmd_str[1], cmd_str[2])
        elif cmd_str[0] == 'ADD_PRO_MEMBERSHIP':
            command = AddProMember()
        elif cmd_str[0] == 'APPLY_COUPON':
            command = ApplyCoupon(cmd_str[1])
        elif cmd_str[0] == 'PRINT_BILL':
            command = PrintBill()
        else:
            return

        self.commands.append(command)

    def unregister(self, command):
        self.commands.remove(command)

    def execute(self):
        for command in self.commands:
            command.execute()
