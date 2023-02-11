from src.models.fees import Fee
from src.repository.invoice_repository import InvoiceRepository
from src.repository.program_repository import ProgramRepository
from src.models.coupons import Coupon
import heapq


class ReportService:
    def __init__(self):
        self.invoice_repository = InvoiceRepository()
        self.program_repository = ProgramRepository()

    def calc_discount(self):
        # print(self.program_repository.program_cost_min_heap)
        if len(self.program_repository.program_cost_min_heap) >= Coupon.B4G1_count:
            self.invoice_repository.invoice.coupon_applied = Coupon.coupons[0]
            discounted_book = heapq.heappop(self.program_repository.program_cost_min_heap)
            self.invoice_repository.invoice.coupon_discount = discounted_book.cost
        elif Coupon.coupons[1] in self.invoice_repository.invoice.coupons:
            self.invoice_repository.invoice.coupon_applied = Coupon.coupons[1]
            discount = self.invoice_repository.invoice.sub_total * 0.2
            self.invoice_repository.invoice.coupon_discount = discount
        elif Coupon.coupons[2] in self.invoice_repository.invoice.coupons:
            self.invoice_repository.invoice.coupon_applied = Coupon.coupons[2]
            discount = self.invoice_repository.invoice.sub_total * 0.05
            self.invoice_repository.invoice.coupon_discount = discount
        else:
            self.invoice_repository.invoice.coupon_applied = ""
            self.invoice_repository.invoice.coupon_discount = 0

    def calc_pro_discount(self):
        pro_discount = 0
        # Hack for testing
        # self.invoice_repository.invoice.is_pro_member = True
        if self.invoice_repository.invoice.is_pro_member:
            for program in self.program_repository.program_cost_min_heap:
                curr_cost = program.cost
                curr_name = program.name
                curr_pro_discount_rate = Fee.pro_discount[curr_name]
                curr_pro_discount = curr_cost * curr_pro_discount_rate
                pro_discount += curr_pro_discount

        self.invoice_repository.invoice.pro_discount = pro_discount

    def calc_program_cost(self):
        cost_sum = 0
        for program in self.program_repository.program_cost_min_heap:
            cost_sum += program.cost
        self.invoice_repository.invoice.program_cost = cost_sum

    def calc_enrol_fee(self):
        if self.invoice_repository.invoice.program_cost < Fee.enrolment_fee_threshold:
            self.invoice_repository.invoice.enrol_fee = Fee.extra_fee['ENROL']

    def calc_sub_total(self):

        self.invoice_repository.invoice.sub_total = self.invoice_repository.invoice.program_cost \
                                                    + self.invoice_repository.invoice.pro_fee \
                                                    + self.invoice_repository.invoice.enrol_fee \
                                                    - self.invoice_repository.invoice.pro_discount

    def calc_total(self):
        self.invoice_repository.invoice.total = self.invoice_repository.invoice.sub_total \
                                                - self.invoice_repository.invoice.coupon_discount

    def print_invoice(self):
        self.calc_program_cost()
        self.calc_pro_discount()
        self.calc_enrol_fee()
        self.calc_sub_total()
        self.calc_discount()
        self.calc_total()
        # print(self.invoice_repository.invoice)
        print("SUB_TOTAL %.2f" % self.invoice_repository.invoice.sub_total)
        print("COUPON_DISCOUNT %s %.2f" % (self.invoice_repository.invoice.coupon_applied,
                                           self.invoice_repository.invoice.coupon_discount))
        print("TOTAL_PRO_DISCOUNT %.2f" % self.invoice_repository.invoice.pro_discount)
        print("PRO_MEMBERSHIP_FEE %.2f" % self.invoice_repository.invoice.pro_fee)
        print("ENROLLMENT_FEE %.2f" % self.invoice_repository.invoice.enrol_fee)
        print("TOTAL %.2f" % self.invoice_repository.invoice.total)
