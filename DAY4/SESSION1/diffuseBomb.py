def diffuseBomb(arr, k):
    n = len(arr)

    result = []
    if k > 0:
        for i in range(n):
            sum = 0
            for j in range(k):
                i = (i + 1) % n
                sum += arr[i]
            result.append(sum)
        return result
    elif k < 0:
        for i in range(n):
            sum = 0
            for j in range(-k):
                i = (i - 1) % n
                sum += arr[i]
            result.append(sum)
        return result
    else:
        return [0] * n    
arr = [1, 2, 3, 4] 
print(diffuseBomb(arr, -2))