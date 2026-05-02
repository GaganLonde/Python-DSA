def kLargest(arr, k):
    arr = sorted(arr)
    l, r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2
        if mid == k:
            return arr[mid - 1]
        if mid < k:
            l = mid + 1
        else:
            r = mid - 1

arr = [5, 6, 1, 7, 8, 10, 11]
print(kLargest(arr, 3))
    
    