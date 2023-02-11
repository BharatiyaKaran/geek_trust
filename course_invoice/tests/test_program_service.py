import unittest

from src.services.program_service import ProgramService


class TestProgramService(unittest.TestCase):
    def setUp(self) -> None:
        self.program_service = ProgramService()
        self.program_service.add_program('CERTIFICATION', 3000)

    def test_add_program_name(self):
        name = self.program_service.program_repository.program_cost_min_heap[0].name
        self.assertEqual(name, 'CERTIFICATION', "Program name not added correctly")

    def test_add_program_cost(self):
        cost = self.program_service.program_repository.program_cost_min_heap[0].cost
        self.assertEqual(cost, 3000, "Program cost not added correctly")
