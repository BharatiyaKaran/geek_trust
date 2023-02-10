from .command import Command
from dataclasses import dataclass, field
from src.models import PassengerType
from src.models import StationName
from src.services import TripService


@dataclass
class CheckInCommand(Command):
    metro_card_id: str
    passenger_type: PassengerType
    station_name: StationName

    def execute(self):
        #print("Checkin command: ", self.metro_card_id, self.passenger_type, self.station_name)
        TripService.add_trip(self.metro_card_id , self.passenger_type, self.station_name)
