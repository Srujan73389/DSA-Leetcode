class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        one_bef,two_bef=1,1
        total=0
        for i in range(2,n+1):
            total=one_bef+two_bef
            two_bef=one_bef
            one_bef=total
            
        return total
            

        