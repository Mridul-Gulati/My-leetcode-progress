class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero = []
        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(nums[i])
            else:
                non_zero.append(nums[i])
        nums[:] = non_zero[:] + zero[:]
        return nums