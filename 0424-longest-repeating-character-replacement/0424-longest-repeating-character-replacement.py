from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        counts=defaultdict(int)
        max_len=0
        majority=0
        while r<len(s):
            counts[s[r]]+=1
            majority=max(majority,counts[s[r]])
            while majority+k<r-l+1:
                counts[s[l]]-=1
                l+=1
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len

        