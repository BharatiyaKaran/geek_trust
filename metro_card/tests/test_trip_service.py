import unittest

from src.services import TripService


class TestTripService(unittest.TestCase):

    def test_calc_discount(self):
        mc_id, station, charge = 'MC2', 'CENTRAL', 500
        discount = TripService.calc_discount(mc_id, station, charge)
        self.assertEqual(discount, 0, "Incorrect discount")

    def test_calc_service_charge(self):
        mc_id, charge = 'MC2', 500
        service_charge = TripService.calc_service_charge(mc_id, charge)
        self.assertEqual(service_charge, 0, "Incorrect service charge")

