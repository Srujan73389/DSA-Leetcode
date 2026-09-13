class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        if len(p)>len(s):
            return res
        p_count=[0]*26
        window_count=[0]*26
        for ch in p:
            p_count[ord(ch)-97]+=1
        for i in range(len(s)):
            window_count[ord(s[i])-97]+=1
            if i>=len(p):
                window_count[ord(s[i-len(p)])-97]-=1
            if p_count==window_count:
                res.append(i-len(p)+1)
        return res
        