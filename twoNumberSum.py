def twoNumberSum(array, targetSum):
    storage = set(num for num in array)
    print(storage, "Here is it")
    for num in array:
    	target = targetSum - num
    	if target in storage and target is not num:
    		return [num,target]

    return []

print(twoNumberSum([2,3,5,4,2], 6))