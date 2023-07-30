class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        s=cmp(x,0)
        x = s*x
        while x>0:
            last = x%10
            ans = (ans*10)+last
            x=x//10
        return s*ans * (s*ans<2**31) * (s*ans>-2**31)
        