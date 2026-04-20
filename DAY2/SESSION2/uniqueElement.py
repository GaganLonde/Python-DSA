def uniqueElement(arr):
    result = 0
    for i in arr:
        result = result ^ i
    return result

#print(uniqueElement([1,2,1,6]))

def uniqueElement2(arr):
    result = []
    for i in arr:
        if i in result:
            result.remove(i)
        else:
            result.append(i)
    return result

#print(uniqueElement2([1,2,1,2,4,6]))

def uniqueElement2_1(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
    diff_bit = xor & ~xor
    a = 0
    b = 0
    for i in arr:
        if i ^ diff_bit == 0:
            a = a ^ i
        else:
            b = b ^ i
    return a, b

print(uniqueElement2_1([1,2,1,2,4,6]))
