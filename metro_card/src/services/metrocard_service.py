class MetroCardService:
    mc_balance_map = dict()
    mc_last_station_map = dict()

    def add_balance(mc_id, amount):
        #print("Add balance: ", mc_id, " : ", amount)
        #print(MetroCardService.mc_balance_map)
        if mc_id in MetroCardService.mc_balance_map.keys():
            MetroCardService.mc_balance_map[mc_id] += int(amount)
        else:
            MetroCardService.mc_balance_map[mc_id] = int(amount)

    def get_all_balance():
        for key, value in MetroCardService.mc_balance_map.items():
            print("Metro Card: ", key, " , Balance: ", value)

    def update_last_station(mc_id, station_name):
        MetroCardService.mc_last_station_map[mc_id] = station_name
