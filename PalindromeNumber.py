class Solution(object):
    def isPalindrome(self, x):
        rev=0
        n=x
        while(n>0):
            rem=n%10
            rev=rev*10+rem
            n=n//10
        return rev==x
        if x<0:
            return False