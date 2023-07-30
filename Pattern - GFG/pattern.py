#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        j=N-1
        for i in range(1,N+1):
            print(" "*j+"* "*i)
            j-=1
        k=0
        for i in range(N,0,-1):
            print(" "*k+"* "*i)
            k+=1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printDiamond(N)
# } Driver Code Ends