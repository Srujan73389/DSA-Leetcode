class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch.isdigit():
                st.pop()
            else:
                st+=ch
        return "".join(st)
        