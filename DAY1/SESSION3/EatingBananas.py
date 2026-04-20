from math import * 
def eatBananas(h,piles):
    
    def possible(k):
        hours = 0
        for p in piles:
            hours += ceil(p / k)
        return hours <= h
    
    l, r = 1, max(piles)
    while l < r:
        mid = (l + r) // 2
        if possible(mid):
            r = mid
        else:
            l = mid + 1
    return l

print(eatBananas(6, [5, 8, 10]))