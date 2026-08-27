from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=defaultdict(int)
        for char in t:
            d[char]+=1
        l=r=0
        formed,total=0,len(d)
        min_len=float('inf')
        minl,maxl=0,0
        while r<len(s):
            char=s[r]
            if char in d:
                d[char]-=1
                if d[char]==0:
                    formed+=1
            while l<=r and formed==total:
                curr_len=r-l+1
                if curr_len<min_len:
                    min_len=curr_len
                    minl,maxl=l,r+1
                char=s[l]
                if char in d:
                    if d[char]==0:
                        formed-=1
                    d[char]+=1
                l+=1
            r+=1
        return "" if min_len==float('inf') else s[minl:maxl]

        