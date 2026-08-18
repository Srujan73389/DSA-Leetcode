class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for n in s:
            count[n]=count.get(n,0)+1
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1
        