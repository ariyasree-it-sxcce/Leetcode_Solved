def reverseVowels(s):
        x=list(s) #['I','c','e','C','r','e','A','m']
        vowels= ['a','A','e','E','i','I','o','I','u','U']
        l=0
        r=len(x)-1
        while l<r:
            if x[l] not in vowels:
                l+=1
            elif x[r] not in vowels:
                r-=1
            else:
                x[l],x[r]=x[r],x[l]
                l+=1
                r-=1
        return "".join(x)
print(reverseVowels("IceCreAm"))