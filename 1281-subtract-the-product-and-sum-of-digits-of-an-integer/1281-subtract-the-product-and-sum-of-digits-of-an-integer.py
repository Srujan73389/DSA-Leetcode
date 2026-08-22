class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        prod=1
        while n>0:
            digit=n%10
            n//=10
            summ+=digit
            prod*=digit
        return prod-summ
        