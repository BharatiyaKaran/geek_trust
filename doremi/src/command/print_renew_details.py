from src.command.command import Command
from src.services.renewal_service import RenewalService


class PrintRenewDetails(Command):

    def execute(self):
        renewal_service = RenewalService()
        renewal_service.print_renewal_details()
