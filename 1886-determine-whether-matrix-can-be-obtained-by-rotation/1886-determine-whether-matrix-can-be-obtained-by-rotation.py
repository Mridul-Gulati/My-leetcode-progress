class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        
        for i in range(4):
            mat[:] = mat[::-1]
            mat[:] = [list(col) for col in zip(*mat)]
            if mat == target:
                return True
        return False