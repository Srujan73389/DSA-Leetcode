class Solution:

    def palindrome(self,s,l,r):
        count=0
        while(l>=0 and r<len(s) and s[l]==s[r]):
            count+=1
            l-=1
            r+=1
        return count            
    def countSubstrings(self, s: str) -> int:
        counts=0
        for i in range(len(s)):
            counts+=self.palindrome(s,i,i)
            counts+=self.palindrome(s,i,i+1)
        return counts
        