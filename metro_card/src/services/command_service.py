from src.command import CommandRegistry


class CommandService:

    def __init__(self):
        self.command_registry = CommandRegistry()

    def register(self, lines):
        for line in lines:
            self.command_registry.register(line)

    def execute(self):
        self.command_registry.execute()