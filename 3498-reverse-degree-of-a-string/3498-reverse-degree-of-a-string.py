class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i,ch in enumerate(s):
            alphabet=ord(ch)-97+1
            rev=27-alphabet
            position=i+1
            mul=rev*position
            total+=mul
        return total

       

            
        