from src.models.trip import Trip
from src.models.charges import Charge
from .metrocard_service import MetroCardService
from .station_service import StationService


class TripService:
    trips = []

    @staticmethod
    def calc_service_charge(mc_id, charge):
        service_charge = 0
        if mc_id in MetroCardService.mc_balance_map.keys():
            balance = MetroCardService.mc_balance_map[mc_id]
            if charge > balance:
                service_charge = (charge - balance) * Charge.service_charge

        return int(service_charge)

    @staticmethod
    def calc_discount(mc_id, station, charge):
        # check if mc_id is present
        if mc_id in MetroCardService.mc_last_station_map.keys():
            # if the last origin station is not same as current station
            # => return journey, hence discount
            if MetroCardService.mc_last_station_map[mc_id] != station:
                # 50% discount on round trip
                return int(charge * 0.5)

        return 0

    @staticmethod
    def add_trip(mc_id, passenger_type, station_name):
        charge = Charge.travel_charge[passenger_type]
        discount = TripService.calc_discount(mc_id, station_name, charge)
        charge_with_discount = charge - discount
        service_charge = TripService.calc_service_charge(mc_id, charge_with_discount)
        amount = charge_with_discount + service_charge

        # update metro card balance, assumption: present
        MetroCardService.mc_balance_map[mc_id] -= amount

        # set balance to 0 when negative, expect to recharge before next trip
        if MetroCardService.mc_balance_map[mc_id] < 0:
            MetroCardService.mc_balance_map[mc_id] = 0

        # update station map
        StationService.update_station_map(station_name, amount,
                                          discount, passenger_type)

        # update last station for discount
        # If round trip completed, got discount, then delete the last station from map
        if discount:
            MetroCardService.mc_last_station_map.pop(mc_id)
        else:
            MetroCardService.mc_last_station_map[mc_id] = station_name

        # Create a trip object and save it for further analytics purpose.s
        trip = Trip(mc_id, amount, service_charge, discount, passenger_type, station_name)
        # Add trip to the list of trips
        TripService.trips.append(trip)
