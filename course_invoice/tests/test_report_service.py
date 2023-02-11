import unittest

from src.services.program_service import ProgramService
from src.services.report_service import ReportService


class TestReportService(unittest.TestCase):
    def setUp(self) -> None:
        self.report_service = ReportService()
        self.program_service = ProgramService()
        self.program_service.add_program('CERTIFICATION', 3000)

    def test_calc_program_cost(self):
        # TODO: Fix test
        self.report_service.calc_program_cost()
        curr_sum = self.report_service.invoice_repository.invoice.program_cost
        self.assertEqual(curr_sum, 27000000, "Incorrect program cost")
