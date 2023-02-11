from dataclasses import dataclass


@dataclass
class Program:
    name: str
    cost: int

    def __lt__(self, other):
        return self.cost < other.cost
