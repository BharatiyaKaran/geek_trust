from .command import Command
from src.services import StationService


class PrintCommand(Command):
    def execute(self):
        #print("Print command: ")
        StationService.generate_report()