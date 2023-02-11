from dataclasses import dataclass
from .station_name import StationName


@dataclass
class Station:
    collection: int
    discount: int
    name: StationName
    passenger_count_map: dict()

    # for sorting the station by name
    def __lt__(self, other):
        return self.name < other.name
