class Solution:
    def makeFancyString(self, s: str) -> str:
        answr=""
        for ch in s:
            if len(answr)<2 or answr[-1]!=ch or answr[-2]!=ch:
                answr+=ch
        return answr 
        