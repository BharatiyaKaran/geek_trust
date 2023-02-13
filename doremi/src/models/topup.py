class TopUp:
    has_duplicate = False

    COST = {
        'FOUR_DEVICE': 50,
        'TEN_DEVICE': 100
    }

    def __init__(self, type: str, count: int, cost: int, is_duplicate: bool):
        self.type = type
        self.count = count
        self.cost = cost
        self.is_duplicate = is_duplicate
