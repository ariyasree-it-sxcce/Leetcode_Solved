class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        right=0
        minimum=[]
        sum=0
        while right < len(nums):
            sum = sum + nums[right]
            while sum >= target:
                minimum.append(right-left+1)
                sum-=nums[left]
                left+=1
            right+=1
        return 0 if len(minimum)==0 else min(minimum)
    
    # Time complexity O(n) as it checks and move right and left pointer for n times,
'''          
         -> Even though there are two loops, the total work is linear because the inner loop 
          doesn’t restart for every outer iteration - it just continues moving left forward.
 '''

    # Space Complexity O(1) as it returns minimum of one value