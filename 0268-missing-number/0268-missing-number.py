class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = [value for value in range(n+1)]
        missing = 0
        for i in ans:
            if i not in nums:
                return i
           