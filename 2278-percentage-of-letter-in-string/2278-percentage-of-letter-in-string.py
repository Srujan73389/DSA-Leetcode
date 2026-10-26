class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        for i in range(len(s)):
            if letter==s[i]:
                count+=1
        return int((count/len(s))*100)
            
        