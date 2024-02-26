class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # So we have one middle pointer and
        # if current number is less than
        # target than move up / otherwise if it's greater move down
        low, high = 0, len(nums) - 1

        while low<=high:
            mid = low + (high-low) // 2
            value = nums[mid]

            if value < target:
                low = mid + 1
            elif value > target:
                high = mid - 1
            else:
                return mid
        
        return -1