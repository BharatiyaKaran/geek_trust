from dataclasses import dataclass, field


@dataclass
class Invoice:
    coupons: list = field(default_factory=list[str])
    program_cost: float = 0
    is_pro_member: bool = False
    sub_total: float = 0
    coupon_applied: str = 'NONE'
    coupon_discount: float = 0
    pro_discount: float = 0
    pro_fee: float = 0
    enrol_fee: float = 0
    total: float = 0

