def longestSusbstring(str):
    l = 0
    max_sub = 0
    s_sub = []

    for r in range(len(str)):
        if str[r] in s_sub:
            s_sub.remove(s_sub[l])
            l += 1
        
        window = r-l+1
        s_sub.append(str[r])
        max_sub = max(max_sub, window)
    
    return max_sub

str = "abcabcbb"
print(longestSusbstring(str))
