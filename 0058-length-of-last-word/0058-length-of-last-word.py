class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        a=s.split(" ")
        return len(a[-1])
        
        