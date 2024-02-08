def threeSum(nums):
    res = []
    nums.sort()

    for index, value in enumerate(nums):
        if index > 0 and value == nums[index-1]:
            continue
        
        l,r = index + 1, len(nums) - 1
        while l<r:
            threeSum = value + nums[l] + nums[r]

            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                res.append([value, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res
