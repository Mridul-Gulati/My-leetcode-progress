class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        count=0
        b = nums
        while val in nums:
            a=nums.index(val)
            nums[a]='a'
            count+=1
        while(count>0):    
            b.remove('a')
            count-=1
        return len(b)