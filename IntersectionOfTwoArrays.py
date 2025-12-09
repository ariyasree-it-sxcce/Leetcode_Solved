class Solution(object):
    def intersection(self, nums1, nums2):
        x=set(nums1)
        y=set(nums2)
        result=x.intersection(y)
        return list(result)