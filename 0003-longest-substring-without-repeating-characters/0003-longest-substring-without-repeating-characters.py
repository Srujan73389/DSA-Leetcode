class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=right=0
        d={}
        leng=0
        while right<len(s):
            if s[right] in d and d[s[right]]>=left:
                left=d[s[right]]+1
            leng=max(leng,right-left+1)
            d[s[right]]=right
            right+=1
        return leng
        