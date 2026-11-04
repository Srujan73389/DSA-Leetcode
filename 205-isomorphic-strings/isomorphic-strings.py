class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1={}
        map_2={}
        for i in range(len(s)):
            if s[i] in map_1:
                if map_1[s[i]]!=t[i]:
                    return False
            else:
                map_1[s[i]]=t[i]

            if t[i] in map_2:
                if map_2[t[i]]!=s[i]:
                    return False
            else:
                map_2[t[i]]=s[i]
        return True
        