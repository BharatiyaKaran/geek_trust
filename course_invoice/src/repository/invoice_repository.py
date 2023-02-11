from singleton_decorator import singleton

from src.models.fees import Fee
from src.models.invoice import Invoice


@singleton
class InvoiceRepository:
    def __init__(self):
        self.invoice = Invoice()

    def update_pro_membership(self):
        self.invoice.is_pro_member = True
        self.invoice.pro_fee = Fee.extra_fee['PRO']

    def add_coupon(self, coupon_name):
        self.invoice.coupons.append(coupon_name)

