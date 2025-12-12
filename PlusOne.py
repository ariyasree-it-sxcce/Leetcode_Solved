class Solution(object):
    def plusOne(self, digits):
        sum=0
        for i in digits:
            sum=sum*10+i
        sum+=1

        result=[]
        while sum>0:
            digit=sum%10
            result.append(digit)
            sum=sum//10
        result.reverse()
        return result