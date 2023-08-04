class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        n = len(nums)
        ans = []
        for i in range(n):
            rem = target - nums[i]
            if rem in d.keys():
                 return [d[rem],i]
            d[nums[i]] = i
        