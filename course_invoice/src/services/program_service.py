from singleton_decorator import singleton

from src.models.program import Program
from src.models.fees import Fee
from src.repository.program_repository import ProgramRepository


@singleton
class ProgramService:
    def __init__(self):
        self.program_repository = ProgramRepository()

    def add_program(self, program_name: str, count: int):
        for i in range(int(count)):
            program = Program(program_name, Fee.program_fee[program_name])
            self.program_repository.add_program(program)
