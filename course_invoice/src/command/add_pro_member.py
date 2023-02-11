from src.command.command import Command
from src.services.invoice_service import InvoiceService


class AddProMember(Command):

    def execute(self):
        invoice_service = InvoiceService()
        invoice_service.update_pro_membership()