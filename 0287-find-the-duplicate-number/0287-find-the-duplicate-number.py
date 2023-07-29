class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        a.sort()
         
        for i in range(len(nums)):
            if a[i] == a[i+1]:
                return a[i]
            