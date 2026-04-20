def ATM(balance, amount, type):
    if amount > 50000:
        print("EXCEEDS MAXIMUM LIMIT")
        return
    
    if amount % 100 != 0:
        print("NOT A MULTIPLE OF 100")
        return
    
    if type == 1:
        if balance - amount < 500:
            print("INSUFFICIENT BALANCE")
            return
    elif type == 2:
        if amount > 25000:
            balance = balance - amount - 50
            print("BALANCE: ", balance)
            return

    balance = balance - amount
    print("SUCCESS!, NEW BALANCE: ", balance)

ATM( balance=50000, amount=30000, type=2)