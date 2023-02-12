from singleton_decorator import singleton

@singleton
class TopUpRepository:
    def __init__(self):
        self.topup = []