class Fee:
    extra_fee = {
        'ENROL': 500,
        'PRO': 200
    }

    # program fee in rupees(INR)
    program_fee = {
        'CERTIFICATION': 3000,
        'DEGREE': 5000,
        'DIPLOMA': 2500
    }

    # pro membership discount percent(%)
    pro_discount = {
        'CERTIFICATION': 0.02,  # 2%
        'DEGREE': 0.03,         # 3%
        'DIPLOMA': 0.01         # 1%
    }

    # enrolment fee threshold
    enrolment_fee_threshold = 6666