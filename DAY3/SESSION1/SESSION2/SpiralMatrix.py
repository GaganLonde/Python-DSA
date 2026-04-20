def spiralMatrix(arr):
    n = len(arr)
    m = len(arr[0])

    result = []
    direction = "r"
    right_wall = m
    down_wall = n
    up_wall = 0
    left_wall = -1

    i , j = 0, 0
    
    while (up_wall<=down_wall and left_wall<=right_wall):
        if direction == "r":
            while j < right_wall:
                result.append(arr[i][j])
                j += 1

            right_wall -= 1
            direction = "d"
            i, j = i + 1, j - 1

        elif direction == "d":
            while i < down_wall:
                result.append(arr[i][j])
                i += 1
            down_wall -= 1
            direction = "l"
            i, j = i - 1, j - 1

        elif direction == "l":
            while j > left_wall:
                result.append(arr[i][j])
                j -= 1
            left_wall += 1
            direction = "u"
            i, j = i - 1, j + 1

        elif direction == "u":
            while i > up_wall:
                result.append(arr[i][j])
                i -= 1
            up_wall += 1
            direction = "r"
            i, j = i + 1, j + 1
    return result

print(spiralMatrix([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]))


print(spiralMatrix([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]]))

print(spiralMatrix([[1, 2],
                    [3, 4],
                    [5, 6]]))