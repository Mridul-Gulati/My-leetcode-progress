class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=defaultdict(list)
        for i in strs:
            res[str(sorted(i))].append(i)
        a=list(res.values())
        return a