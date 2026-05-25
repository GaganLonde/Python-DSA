def numDecodings(str):
    if not str or str[0] == '0':
        return 0
    
    # dp[i-2], dp[i-1], dp[i]
    prev2, prev1 = 1, 1
    
    for i in range(1, len(str)):
        curr = 0
        
        # Check single digit decoding
        if str[i] != '0':
            curr += prev1
            
        # Check two digits decoding
        two_digit = int(str[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2
            
        # Move pointers
        prev2, prev1 = prev1, curr
        
    return prev1

# print(numDecodings("12152145"))
# print(numDecodings("226"))
# print(numDecodings("999"))
print(numDecodings("1212"))
#12152145
