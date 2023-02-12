class TopUp:
    add_topup_fail = False
    add_topup_fail_reason = ''

    COST = {
        'FOUR_DEVICE': 50,
        'TEN_DEVICE': 100
    }

    def __init__(self, type: str, count: int):
        self.type = type
        self.count = count