class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            res=[]
            for i in range(0,len(s),k):
                end=min(i+k,len(s))
                total=sum(int(c) for c in s[i:end])
                res.append(str(total))
            s=''.join(res)
        return s