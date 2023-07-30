#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        j=0
        for i in range(2*N-1,0,-2):
            print(" "*j+"*"*i)
            j+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends