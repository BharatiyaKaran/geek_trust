from src.command.command import Command
from src.services.report_service import ReportService


class PrintBill(Command):

    def execute(self):
        report_service = ReportService()
        report_service.print_invoice()