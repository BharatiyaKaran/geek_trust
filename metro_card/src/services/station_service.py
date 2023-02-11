from src.models.station import Station


class StationService:
    # map of station_name: station objects
    station_map = dict()

    @staticmethod
    def update_station_map(station_name, amount, discount, passenger_type):
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

    @staticmethod
    def generate_report():
        # sort the passengers in descending order of count
        for key, value in StationService.station_map.items():
            sorted_passenger_count_map = sorted(value.passenger_count_map.items(),
                                                key=lambda x: (x[1] * -1, x[0]))
            value.passenger_count_map = dict(sorted_passenger_count_map)

        # print final output
        # sort station by name to always keep "CENTRAL' above 'AIRPORT'
        sorted_station_map = sorted(StationService.station_map.items(),
                                    key=lambda x: x[1], reverse=True)
        StationService.station_map = dict(sorted_station_map)
        for key, value in StationService.station_map.items():
            print("TOTAL_COLLECTION ", key, value.collection, value.discount)
            print("PASSENGER_TYPE_SUMMARY ")
            for key, value in value.passenger_count_map.items():
                print(key, value)
