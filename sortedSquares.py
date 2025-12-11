class Solution(object):
    def sortedSquares(self, nums):
        A=[]
        for i in range(0,len(nums)):
            x=nums[i]*nums[i]
            A.append(x)
        return sorted(A)
    
# Time Complexity ---> O(n)+O(n log n) ===> Therefore, O(n log n)
#Space Complexity ---> O(n)

'''
ANOTHER APPROACH

def sortedArray(nums):
    A=[]
    temp=0
    for i in nums:
        x=i*i
        A.append(x)
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if A[i]>A[j]:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
    return A
print(sortedArray([-4,-1,0,3,10]))


Time Complexity ---> O(n^2)
Space Complexity ---> O(n)
'''