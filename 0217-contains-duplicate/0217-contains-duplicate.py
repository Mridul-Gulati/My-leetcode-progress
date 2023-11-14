class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if list(sorted(set(nums))) == sorted(nums):
            return False
        print(list(set(nums)))
        return True
        