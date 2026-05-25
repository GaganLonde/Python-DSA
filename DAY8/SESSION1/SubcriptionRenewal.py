def longest_window(days, k):
    l = 0
    max_len = 0
    for r in range(len(days)):
        while days[r]-days[l]>k:
            l+=1
        max_len = max(max_len, r-l+1)
    return max_len

days = [1, 3, 5, 7, 9]
k = 4
print(longest_window(days, k))



    

