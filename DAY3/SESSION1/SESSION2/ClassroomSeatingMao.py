def  seatingMap(arr):
    empty = 0
    occupied = 0
    for i in arr:
        for j in i:
            if j == 0:
                empty += 1
            else:
                occupied += 1
            

    return (empty, occupied)

print(seatingMap([[1, 0, 0], [0, 1, 1], [0, 0, 0]]))