from datetime import datetime

from src.command.command import Command
from src.services.subscription_service import SubscriptionService


class StartSubscription(Command):
    def __init__(self, start_date: datetime):
        self.start_date = start_date

    def execute(self):
        subscription_service = SubscriptionService()
        subscription_service.start_subscription(self.start_date)


