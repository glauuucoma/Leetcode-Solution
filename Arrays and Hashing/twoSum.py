# Stupid solution O T(n^2), O S(N)

def twoSum1(self, nums, target):
	neededValue = 0
	cutNums = nums.copy()
	for i in range(len(nums)):
		neededValue = target - nums[i]
		cutNums = nums[:i] + nums[i+1:]
		try:
			return [i, cutNums.index(neededValue) + 1]
		except:
			pass

# Normal solution using Hash Maps O T(n), O S(n)
# In this example I will be using hashmaps
# I will iterate throught list, append the element's difference
# with target to dictionary key

	
def twoSum(nums, target):
	neededValue, neededValuesDict = 0, {}
	for idx, elm in enumerate(nums):
		neededValue = target - elm
		if neededValue in neededValuesDict:
			return [idx, neededValuesDict[neededValue]]
		neededValuesDict[elm] = idx
