class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[1]*(n+1)
        arr[0]=0
        if n>1:
            for i in range(2,n+1):            
                arr[i] = arr[i-1] + arr[i-2]
        return arr[n]