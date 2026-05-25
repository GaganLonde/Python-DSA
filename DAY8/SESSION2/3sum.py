def threeSum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            sol = nums[i] + nums[l] + nums[r]
            if sol == 0:
                ans.append([nums[i], nums[l], nums[r]])
                l, r = l + 1, r - 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif sol < 0:
                l += 1
            else:
                r -= 1
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
            
            