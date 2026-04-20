def ticketPrice(day, show_time, age, seat):
    base_price = 200
    total_price = base_price
    weak_day_disc = 0
    age_disc = 0
    surchage = 0
    GST = 0
    if day <= 4:
        weak_day_disc = base_price * 0.2
        total_price = base_price - weak_day_disc
    if age < 12 or age > 60:
        age_disc = total_price * 0.3
        total_price = total_price - age_disc
    if seat == 1:
        surchage = 0
        pass
    elif seat == 2:
        surchage = 100
        total_price += 100
    elif seat == 3:
        surchage = 250
        total_price += 250
    if total_price > 500:
        GST = total_price * 0.18
        total_price += GST
    else:
        GST = total_price * 0.12
        total_price += GST

    print(f"WeekDay Disc: {weak_day_disc} | Age Disc: {age_disc} | Surcharge: {surchage} | GST: {GST} | Total: {total_price}")

# ticketPrice(2, 18, 25, 1)
# ticketPrice(6, 20, 10, 3)
# ticketPrice(7, 20, 30, 3)
ticketPrice(3, 14, 8, 1)