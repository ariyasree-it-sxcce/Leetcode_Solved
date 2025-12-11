class Solution(object):
    def sortedSquares(self, nums):
        A=[]
        for i in range(0,len(nums)):
            x=nums[i]*nums[i]
            A.append(x)
        return sorted(A)