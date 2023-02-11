from dataclasses import dataclass

from src.command.command import Command
from src.services.program_service import ProgramService


@dataclass
class AddProgram(Command):
    name: str
    count: int

    def execute(self):
        program_service = ProgramService()
        program_service.add_program(self.name, self.count)
