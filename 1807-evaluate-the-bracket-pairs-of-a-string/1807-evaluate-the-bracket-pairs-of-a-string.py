class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = dict(knowledge)
        i=0
        n=len(s)
        res=[]
        while i<n:
            if s[i]=='(':
                i+=1
                key=""
                while i<n and s[i]!=')':
                    key+=s[i]
                    i+=1
                res.append(mp.get(key,"?"))
            else:
                res.append(s[i])
            i+=1
        return ''.join(res)

        