class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_m=set()
        for i in s:
            if i in hash_m:
                return i
            hash_m.add(i)