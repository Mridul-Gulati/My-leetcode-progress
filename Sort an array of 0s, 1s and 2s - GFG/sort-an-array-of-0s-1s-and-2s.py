#User function Template for python3


class Solution:
        
    def sort012(self,arr,n):
        count_0, count_1, count_2 = 0, 0, 0
        for i in arr:
            if i == 0:
                count_0 += 1
            elif i == 1:
                count_1 += 1
            else:
                count_2 += 1
        temp0 = [0]*count_0
        temp1 = [1]*count_1
        temp2 = [2]*count_2
        
        temp = temp0 + temp1 + temp2
        
        for f in range(n):
            arr[f] = temp[f]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends