class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        d={piece[0]:piece for piece in pieces}
        res=[]
        for x in arr:
            if x in d:
                res.extend(d[x])
        return res==arr
        