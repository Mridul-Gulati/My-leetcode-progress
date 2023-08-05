class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        sum_num = 0
        count = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            rem = sum_num - k
            if rem in d:
                count+=d[rem]
            if sum_num not in d:
                d[sum_num] = 1
            else:
                d[sum_num] += 1
        return count