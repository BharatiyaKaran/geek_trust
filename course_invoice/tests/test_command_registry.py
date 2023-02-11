import unittest

from src.command import CommandRegistry
from src.command.add_pro_member import AddProMember
from src.command.apply_coupon import ApplyCoupon
from src.command.print_bill import PrintBill


class TestCommandRegistry(unittest.TestCase):
    def setUp(self) -> None:
        self.command_registry = CommandRegistry()

    def test_add_program_command(self):
        cmd_str = "ADD_PROGRAMME CERTIFICATION 1"
        self.command_registry.register(cmd_str)
        add_program_command = self.command_registry.commands[0]
        self.assertEqual(add_program_command.name, 'CERTIFICATION',
                         'CERTIFICATION program not added')

    def test_add_pro_member_command(self):
        cmd_str = "ADD_PRO_MEMBERSHIP"
        self.command_registry.register(cmd_str)
        add_pro_member = self.command_registry.commands[0]
        self.assertIsInstance(add_pro_member, AddProMember,
                              'ADD_PRO_MEMBERSHIP not registered')

    def test_apply_coupon_command(self):
        cmd_str = "APPLY_COUPON DEAL_G20"
        self.command_registry.register(cmd_str)
        apply_coupon = self.command_registry.commands[0]
        self.assertIsInstance(apply_coupon, ApplyCoupon,
                              'APPLY_COUPON not registered')

    def test_print_bill_command(self):
        cmd_str = "PRINT_BILL"
        self.command_registry.register(cmd_str)
        print_bill = self.command_registry.commands[0]
        self.assertIsInstance(print_bill, PrintBill,
                              'PRINT_BILL not registered')
