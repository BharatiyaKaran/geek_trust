from dataclasses import dataclass
from .station_name import StationName


@dataclass
class Station:
    collection: int
    discount: int
    name: StationName
    passenger_count_map: dict()
