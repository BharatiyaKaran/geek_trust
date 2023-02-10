from dataclasses import dataclass
from .passenger_type import PassengerType
from .station_name import StationName


@dataclass
class Trip:
    mc_id: str
    amount: int
    service_charge: int
    discount: int
    passenger: PassengerType
    from_station: StationName


