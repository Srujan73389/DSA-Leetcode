class Solution(object):
    def isAnagram(self, s, t):
        s_h={}
        t_h={}
        for i in s:
            s_h[i]=s_h.get(i,0)+1
        for i in t:
            t_h[i]=t_h.get(i,0)+1
        return s_h==t_h

        
        