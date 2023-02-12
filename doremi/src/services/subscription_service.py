from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

from singleton_decorator import singleton

from src.models.plan import Plan
from src.models.subscription import Subscription
from src.models.topup import TopUp
from src.repository.subscription_repository import SubscriptionRepository


@singleton
class SubscriptionService:
    def __init__(self):
        self.subscription_repo = SubscriptionRepository()
        self.date_format = '%d-%m-%Y'

    def start_subscription(self, start_date: datetime):
        try:
            Subscription.start_date = datetime.strptime(start_date, self.date_format).date()

        except ValueError:
            #print("Incorrect date format")
            Subscription.invalid_subscription_date = True
            Subscription.add_subscription_failed_reason = 'INVALID_DATE'
            TopUp.invalid_date = True

    def get_end_date(self, start_date, duration):
        end_date = start_date + relativedelta(months=+duration) \
                   - timedelta(days=Subscription.reminder_threshold)
        end_date = datetime.strptime(str(end_date), '%Y-%m-%d').strftime(self.date_format)
        return end_date

    def add_subscription(self, category, plan):
        cost = Plan.PLANS[category][plan][0]
        duration = Plan.PLANS[category][plan][1]
        end_date = None
        if Subscription.invalid_subscription_date:
            pass
        else:
            end_date = self.get_end_date(Subscription.start_date, duration)
        subscription = Subscription(category, plan, cost, duration, end_date)
        if subscription in self.subscription_repo.subscriptions:
            Subscription.add_subscription_failed = True
            Subscription.add_subscription_failed_reason = 'DUPLICATE_CATEGORY'

        self.subscription_repo.subscriptions.append(subscription)
