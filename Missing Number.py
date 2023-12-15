def missingNumber(nums):
    i = 0
    correctArr = []
    for i in range(len(nums)+1):
        if(i not in nums):
            return i

print(missingNumber([3,0,1]))
