class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        left=0
        right=len(nums)-1
        while left <= right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                result.append(nums[left]*nums[left])
                left+=1
            else:
                result.append(nums[right]*nums[right])
                right-=1
        return result