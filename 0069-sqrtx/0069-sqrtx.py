class Solution(object):
    def mySqrt(self, x):
        l=1
        R=x
        while l<=R:
            M=(l+R)//2
            if M*M==x:
                return M
            elif M*M<x:
                l=M+1
            else:
                R=M-1
        return R

        
        