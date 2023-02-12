from src.command.command import Command
from src.services.topup_service import TopUpService


class AddTopUp(Command):
    def __init__(self, type: str, count: int):
        self.type = type
        self.count = count

    def execute(self):
        topup_service = TopUpService()
        topup_service.add_topup(self.type, self.count)
