class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitsh=0xffffffff
        while b&bitsh>0:
            carry=(a&b)<<1
            a=a^b
            b=carry
        return a&bitsh if b>0 else a
        