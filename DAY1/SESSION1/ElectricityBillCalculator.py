def Bill(units):
    if units <= 100:
        total_amount = units * 1.5
    elif units <= 200:
        total_amount = 100 * 1.5 + (units - 100) * 2.5
    else:
        total_amount = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    return total_amount

units = int(input("Enter the number of units consumed: "))
print("Total Electricity Bill: ", Bill(units))

