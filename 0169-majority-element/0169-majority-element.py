class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq.keys():
                freq[i]+=1
            else:
                freq[i] = 1
            if freq[i] > n//2:
                return i

        