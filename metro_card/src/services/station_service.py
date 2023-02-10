from src.models.station import Station


class StationService:
    station_map = dict()

    def update_station_map(station_name, amount, discount, passenger_type):
        # print("update_station_map" , station_name, amount, discount, passenger_type )
        if station_name in StationService.station_map.keys():
            station = StationService.station_map[station_name]
            station.collection += amount
            station.discount += discount
            if passenger_type in station.passenger_count_map.keys():
                station.passenger_count_map[passenger_type] += 1
            else:
                station.passenger_count_map[passenger_type] = 1
        else:
            passenger_count_map = {passenger_type: 1}
            station = Station(amount, discount, station_name, passenger_count_map)
            StationService.station_map[station_name] = station

    def generate_report():
        #print("Generating Final Report ...")
        for key, value in StationService.station_map.items():
            sorted_passenger_count_map = sorted(value.passenger_count_map.items(),
                                                key=lambda x: x[1], reverse=True)
            value.passenger_count_map = dict(sorted_passenger_count_map)
        #print(StationService.station_map)

        for key, value in StationService.station_map.items():
            print("TOTAL COLLECTION ", key, value.collection, value.discount)
            print("PASSENGER TYPE SUMMARY ")
            for key, value in value.passenger_count_map.items():
                print(key, value)
