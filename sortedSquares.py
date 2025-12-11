class Solution(object):
    def sortedSquares(self, nums):
        A=[]
        for i in range(0,len(nums)):
            x=nums[i]*nums[i]
            A.append(x)
        return sorted(A)
    
# Time Complexity ---> O(n)+O(n log n) ===> Therefore, O(n log n)
#Space Complexity ---> O(n)