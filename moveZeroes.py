class Solution(object):
    def moveZeroes(self, nums):
        read=0
        write=0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write],nums[read]=nums[read],nums[write]
                write+=1
                read+=1
            read+=1
        return nums
    
    
# Time Complexity O(n)
# Space Complexity O(n)
'''
    nums=[0,1,0,3,12]

    0	1   0   3   12
    W,R
    R=R+1
    ---------------------
    0	1	 0	3	12
    W   R
    
    Condition R is not equal to 0, 
    hence it swaps with W(That is write non zero to the place of zero and move zero backward)
    
    A[W],A[R]=A[R],A[W]
    W=W+1
    R=R+1
    --------------------- 
    1	0	0	3	12
        W	R

    R=R+1
    ---------------------
    1	0	 0	 3	 12
        W		 R
    A[W],A[R]=A[R],A[W]
    
    1	3	0	0	12
        W		R
    W=W+1
    R=R+1
    ---------------------
    1	3	0	0	12
            W		R
    A[W],A[R]=A[R],A[W]
    
    1	3	12	0	0
            W		R
    
''' 