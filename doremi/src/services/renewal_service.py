from singleton_decorator import singleton

from src.models.subscription import Subscription
from src.models.topup import TopUp
from src.repository.subscription_repository import SubscriptionRepository
from src.repository.topup_repository import TopUpRepository


@singleton
class RenewalService:
    def __init__(self):
        self.subscription_repo = SubscriptionRepository()
        self.topup_repo = TopUpRepository()

    def process_subscription(self):
        if len(self.subscription_repo.subscriptions) == 0:
            print("SUBSCRIPTIONS_NOT_FOUND")
            return 0, -1
        elif Subscription.invalid_subscription_date:
            print("INVALID_DATE")
            for subscription in self.subscription_repo.subscriptions:
                print("ADD_SUBSCRIPTION_FAILED INVALID_DATE")
            return 0, -1
        elif Subscription.add_subscription_failed:
            print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")
            return 0, -1
        else:
            total = 0
            for subscription in self.subscription_repo.subscriptions:
                print("RENEWAL_REMINDER", subscription.category, subscription.reminder_date)
                total += subscription.cost

            return total, 1

    def process_topup(self):
        if TopUp.invalid_date:
            for _ in self.topup_repo.topup:
                print("ADD_TOPUP_FAILED INVALID DATE")
            return 0

        if TopUp.add_topup_fail:
            for _ in self.topup_repo.topup:
                print("ADD_TOPUP_FAILED", TopUp.add_topup_fail_reason)
            return 0
        elif self.topup_repo.topup:
            topup_type = self.topup_repo.topup[0].type
            topup_count = self.topup_repo.topup[0].count
            topup_cost = TopUp.COST[topup_type]
            total_topup_cost = topup_cost * int(topup_count)
            return total_topup_cost
        else:   # No Topups
            return 0

    def print_renewal_details(self):
        subscription_cost, err_sub = self.process_subscription()
        topup_cost = self.process_topup()
        if err_sub != -1:
            total_cost = subscription_cost + topup_cost
            print("RENEWAL_AMOUNT", total_cost)
        if Subscription.invalid_subscription_date:
            print("SUBSCRIPTIONS_NOT_FOUND")
