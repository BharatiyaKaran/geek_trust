from .command import Command
from src.services import StationService


class PrintCommand(Command):
    def execute(self):
        StationService.generate_report()