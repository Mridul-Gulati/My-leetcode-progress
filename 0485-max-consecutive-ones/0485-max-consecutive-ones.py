class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        count_ones = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count_ones += 1
                max_ones = max(max_ones,count_ones)
            else:
                count_ones = 0
        return max_ones