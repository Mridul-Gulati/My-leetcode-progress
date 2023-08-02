class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        b = []
        for i in a:
            b.append(i)
        b.sort()
        for i in range(len(b)):
            nums[i] = b[i]
        return len(a)