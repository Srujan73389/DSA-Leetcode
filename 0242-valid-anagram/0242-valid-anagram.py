class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_h={}
        t_h={}
        for i in s:
            s_h[i]=s_h.get(i,0)+1
        for j in t:
            t_h[j]=t_h.get(j,0)+1
        return s_h==t_h
        