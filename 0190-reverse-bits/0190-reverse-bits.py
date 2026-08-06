class Solution:
    def reverseBits(self, n: int) -> int:
        reversd=0
        for i in range(32):
            reversd=(reversd<<1)|(n&1)
            n>>=1
        return reversd
        