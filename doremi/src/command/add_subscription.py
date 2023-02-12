from src.command.command import Command
from src.services.subscription_service import SubscriptionService


class AddSubscription(Command):
    def __init__(self, category: str, plan: str):
        self.category = category
        self.plan = plan

    def execute(self):
        subscription_service = SubscriptionService()
        subscription_service.add_subscription(self.category, self.plan)
