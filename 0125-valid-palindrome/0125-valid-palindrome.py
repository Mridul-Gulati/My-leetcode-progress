class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        new_s=""
        for i in s:
            if i.isalnum():
                new_s+=i
        print(new_s)
        if new_s[::-1]==new_s:
            return True
        else:
            return False