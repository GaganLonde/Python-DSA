def minNotes(change):
    notes = [100, 50, 20, 10, 5, 2, 1]
    count = 0
    for i in notes:
        count += change // i
        change = change % i
    return count

amount = int(input("Enter the amount: "))
print("Minimum Notes required: ", minNotes(amount))
