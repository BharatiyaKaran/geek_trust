from dataclasses import dataclass
from .station_name import Station


@dataclass
class MetroCard:
    id: str
    balance: int
    last_station: Station
