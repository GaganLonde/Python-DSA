def groceryBill(item, quantity, price, membership):
    sub_total = quantity * price;
    discount = 0
    if membership:
        discount = sub_total * 0.1
    discounted_amt = sub_total - discount
    if discounted_amt > 500:
        gst = discounted_amt * .05
    else:
        gst = discounted_amt * .12
    total = sub_total - discount + gst 
    print(f"Item Name: {item} | Sub-Total: {sub_total} | Discount:  {discount} | GST: {gst} |  Total: {total}")

item = input("Enter the name of the product: ")
quantity = int(input("Enter the quantity: "))
price = float(input("Enetr the price of the item: "))
membership = bool(input("Enter 1 if member else 0: "))

groceryBill(item, quantity, price, membership)