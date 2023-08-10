class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        brr = []
        brr[:] = nums[:]
        brr.sort()
        for i in brr:
            if i == target:
                return True
        return False