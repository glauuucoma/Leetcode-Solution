class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Iterate thru array and count repeating values in dictionary
        traversedElements = {}
        for num in nums:
            if num in traversedElements:
                return True
            else:
                traversedElements[num] = 1
        return False

        # Check whether they are any >1 appereances