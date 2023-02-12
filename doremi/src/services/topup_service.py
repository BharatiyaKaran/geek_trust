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
        if len(self.topup_repo.topup) > 0:
            TopUp.add_topup_fail = True
            TopUp.add_topup_fail_reason = 'DUPLICATE_TOPUP'
        elif len(self.subscription_repo.subscriptions) == 0:
            TopUp.add_topup_fail = True
            TopUp.add_topup_fail_reason = 'SUBSCRIPTIONS_NOT_FOUND'

        self.topup_repo.topup.append(TopUp(type, count))
