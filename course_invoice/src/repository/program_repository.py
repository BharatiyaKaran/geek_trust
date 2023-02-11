from singleton_decorator import singleton

from src.models.program import Program
import heapq


@singleton
class ProgramRepository:
    def __init__(self):
        self.program_cost_min_heap = []

    def add_program(self, program: Program):
        heapq.heappush(self.program_cost_min_heap, program)
