class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        res=nums
        a=[]
        for item in res:
                if (item in freq):
                    freq[item] += 1
                else:
                    freq[item] = 1
        while(k):
            most_frequent_element = max(freq, key=freq.get)
            a.append(most_frequent_element)
            freq[most_frequent_element]=0
            k-=1
        return a