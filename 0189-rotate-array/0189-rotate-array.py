class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        pivot = len(nums) - k
        
        nums[:] = nums[pivot:] + nums[:pivot]
        
        return nums