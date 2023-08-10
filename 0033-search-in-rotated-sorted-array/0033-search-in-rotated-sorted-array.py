class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        brr = []
        brr[:] = nums[:]
        brr.sort()
        if target not in nums:
            return -1
        for i in brr:
            if i==target:
                return nums.index(i)