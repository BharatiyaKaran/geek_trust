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
    """
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
    """

    def process_invalid_date(self):
        print("INVALID_DATE")
        for i in range(len(self.subscription_repo.subscriptions)):
            print("ADD_SUBSCRIPTION_FAILED INVALID_DATE")

        for i in range(len(self.topup_repo.topups)):
            print("ADD_TOPUP_FAILED INVALID_DATE")
        print("SUBSCRIPTIONS_NOT_FOUND")

    def process_duplicate_subscriptions(self):
        for subscription in self.subscription_repo.subscriptions:
            if subscription.is_duplicate:
                print("ADD_SUBSCRIPTION_FAILED DUPLICATE_CATEGORY")

    def process_duplicate_topups(self):
        for topup in self.topup_repo.topups:
            if topup.is_duplicate:
                print("ADD_TOPUP_FAILED DUPLICATE_TOPUP")

    def process_subscriptions(self):
        s_cost = 0
        for subscription in self.subscription_repo.subscriptions:
            if not subscription.is_duplicate:
                s_cost += subscription.cost
                print("RENEWAL_REMINDER", subscription.category, subscription.reminder_date)

        return s_cost

    def process_topups(self):
        t_cost = 0
        for topup in self.topup_repo.topups:
            if not topup.is_duplicate:
                t_cost += topup.cost

        return t_cost

    def print_renewal_details(self):
        if Subscription.invalid_subscription_date:
            self.process_invalid_date()
        else:
            self.process_duplicate_subscriptions()
            self.process_duplicate_topups()
            s_cost = self.process_subscriptions()
            t_cost = self.process_topups()
            total_cost = s_cost + t_cost
            print("RENEWAL_AMOUNT", total_cost)
