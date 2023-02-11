class Coupon:
    B4G1_count = 4
    coupons = ['B4G1', 'DEAL_G20', 'DEAL_G5']
    coupon_discount = {
        'DEAL_G20': 0.2,
        'DEAL_G5': 0.05
    }
    # program cost
    DEAL_G20_threshold = 10000
    # program count
    DEAL_G5_threshold = 2