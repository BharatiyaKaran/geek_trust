class MetroCardService:
    # map of metrocard id: balance amount
    mc_balance_map = dict()
    # map of metrocard id: last station visited
    mc_last_station_map = dict()

    @staticmethod
    def add_balance(mc_id, amount):
        if mc_id in MetroCardService.mc_balance_map.keys():
            MetroCardService.mc_balance_map[mc_id] += int(amount)
        else:
            MetroCardService.mc_balance_map[mc_id] = int(amount)
