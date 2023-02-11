from dataclasses import dataclass

from src.command.command import Command
from src.services.invoice_service import InvoiceService


@dataclass
class ApplyCoupon(Command):
    name: str

    def execute(self):
        invoice_service = InvoiceService()
        invoice_service.add_coupon(self.name)
