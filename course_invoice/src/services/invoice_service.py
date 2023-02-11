from singleton_decorator import singleton

from src.repository.invoice_repository import InvoiceRepository


@singleton
class InvoiceService:
    def __init__(self):
        self.invoice_repository = InvoiceRepository()

    def update_pro_membership(self):
        self.invoice_repository.update_pro_membership()

    def add_coupon(self, coupon_name):
        self.invoice_repository.add_coupon(coupon_name)


