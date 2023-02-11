import unittest

from src.command import CommandRegistry


class TestCommandRegistry(unittest.TestCase):
    def setUp(self) -> None:
        self.command_registry = CommandRegistry()

    def test_balance_command(self):
        cmd_str = "BALANCE MC2 500"
        self.command_registry.register(cmd_str)
        balance_command = self.command_registry.commands[0]
        self.assertEqual(balance_command.metro_card_id, 'MC2',
                         'incorrect metro card id')

    def test_checkin_command(self):
        cmd_str = "CHECK_IN MC1 ADULT CENTRAL"
        self.command_registry.register(cmd_str)
        checkin_command = self.command_registry.commands[0]
        self.assertEqual(checkin_command.metro_card_id, 'MC1',
                         'incorrect metro card id')

    def test_print_command(self):
        cmd_str = "PRINT_SUMMARY"
        self.command_registry.register(cmd_str)
        size = len(self.command_registry.commands)
        self.assertEqual(size, 1,
                         'Print command not registered')
