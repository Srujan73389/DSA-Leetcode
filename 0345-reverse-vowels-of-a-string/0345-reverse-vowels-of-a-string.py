class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels="AEIOUaeiou"
        s=list(s)
        
        i,j=0,len(s)-1
        while i<j:
            if not s[i] in Vowels:
                i+=1
            elif not s[j] in Vowels:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
        