import unittest

from src.services import StationService


class TestTripService(unittest.TestCase):

    def test_update_station_map(self):
        station_name, amount, discount, passenger_type = 'CENTRAL', 500, 100, 'ADULT'
        StationService.update_station_map(station_name, amount, discount, passenger_type)
        result_name = StationService.station_map[station_name].name
        self.assertEqual(result_name, station_name, "Incorrect station created")