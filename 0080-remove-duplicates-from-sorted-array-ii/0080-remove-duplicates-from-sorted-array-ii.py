class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements_count = collections.Counter(nums)
        for key,value in elements_count.items():
            while value>2:
                nums.remove(key)
                value=value-1
        return len(nums)