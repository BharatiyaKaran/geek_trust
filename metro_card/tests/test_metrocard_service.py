import unittest

from src.services import MetroCardService


class TestMetroCardService(unittest.TestCase):

    def test_add_balance(self):
        mc_id, amount = 'MC2', 500
        MetroCardService.add_balance(mc_id, amount)
        balance = MetroCardService.mc_balance_map[mc_id]
        self.assertEqual(balance, 500, "Balance not added")
