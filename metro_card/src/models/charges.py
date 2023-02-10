from .passenger_type import PassengerType


class Charge:
    travel_charge = {
        'ADULT': 200,
        'SENIOR_CITIZEN': 100,
        'KID': 50
    }

    # 2% Service Fee
    service_charge = 0.02
