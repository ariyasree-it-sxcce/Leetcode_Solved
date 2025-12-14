class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers)-1
        while l<r:
            sum=numbers[l]+numbers[r]
            if sum==target:
                x=l+1,r+1
                return list(x)
                break
            elif sum<target:
                l=l+1
            elif sum>target:
                r=r-1
                