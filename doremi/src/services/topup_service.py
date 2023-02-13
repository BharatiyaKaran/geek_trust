from singleton_decorator import singleton

from src.models.topup import TopUp
from src.repository.subscription_repository import SubscriptionRepository
from src.repository.topup_repository import TopUpRepository


@singleton
class TopUpService:
    def __init__(self):
        self.topup_repo = TopUpRepository()
        self.subscription_repo = SubscriptionRepository()

    def add_topup(self, type, count):
        cost = TopUp.COST[type] * int(count)
        curr_topup = TopUp(type, count, cost, False)
        self.topup_repo.topups.append(curr_topup)
        if len(self.topup_repo.topups) > 1:
            TopUp.has_duplicate = True
            curr_topup.is_duplicate = True


