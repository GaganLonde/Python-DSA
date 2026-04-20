def productExceptSelf(arr):
    n = len(arr)
    result = [1] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            result[i] *= arr[j]

    return result

print(productExceptSelf([1,2,3,4]))

def optimisedProductExceptSelf(arr):
    n = len(arr)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] *= prefix
        prefix *= arr[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= postfix
        postfix *= arr[i]

    return result

print(optimisedProductExceptSelf([1,2,3,4]))