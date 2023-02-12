from singleton_decorator import singleton

@singleton
class SubscriptionRepository:
    def __init__(self):
        self.subscriptions = []
