from dataclasses import dataclass, field
from .command import Command
from src.services import MetroCardService


@dataclass
class BalanceCommand(Command):
    metro_card_id: str
    amount: int

    def execute(self):
        MetroCardService.add_balance(self.metro_card_id, self.amount)
