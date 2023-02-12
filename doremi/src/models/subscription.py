from dataclasses import dataclass
from typing import ClassVar
from datetime import date


@dataclass
class Subscription:
    category: str
    plan: str
    cost: int
    duration: int  # months
    reminder_date: date = date.today()
    reminder_threshold: ClassVar[int] = 10              # reminder 10 days before
    start_date: ClassVar[date]  = date.today()          # same for all subscriptions
    invalid_subscription_date: ClassVar[date] = False
    add_subscription_failed: ClassVar[bool] = False
    add_subscription_failed_reason: ClassVar[str]

    def __eq__(self, other):
        return self.category == other.category

    def __hash__(self):
        return hash(self.category)
