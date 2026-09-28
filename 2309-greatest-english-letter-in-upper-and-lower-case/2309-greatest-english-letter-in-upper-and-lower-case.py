class Solution:
    def greatestLetter(self, s: str) -> str:
        curr_ord=0
        res=""
        dic={}
        for ch in s:
            dic[ch]=ord(ch)
        for i in range(len(s)):
            if s[i].islower()==True and s[i].upper() in dic:
                if ord(s[i])>curr_ord:
                    res=s[i].upper()
                    curr_ord=ord(s[i])
        return res
        

        