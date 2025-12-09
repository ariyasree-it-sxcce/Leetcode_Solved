class Solution(object):
    def isHappy(self, n):
        while True:
            if n==1 or n==7:
        
                return True
            elif n<10:
                return False
            else:
                A=0
                while(n>0):
                    mod=n%10
                    A=(mod*mod)+A
                    n=n//10
                n=A
            