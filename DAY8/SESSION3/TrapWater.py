def trapWater(nums):
    n = len(nums)
    sum = 0

    l_wall, r_wall = 0, 0
    max_r = [0] * n
    max_l = [0] * n

    for i in range(n):
        j = -i -1
        max_l[i] = l_wall
        max_r[j] = r_wall
        l_wall = max(l_wall, nums[i])
        r_wall = max(r_wall, nums[j])

    for i in range(n):
        pot = min(max_l[i], max_r[i])
        sum += max(0, pot - nums[i])

    return sum

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
arr2 = [4,2,0,3,2,5]
print(trapWater(arr2))
