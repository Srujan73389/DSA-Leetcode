class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ=0
        prod=1
        original=n
        while n>0:
            digit=n%10
            n//=10
            summ+=digit
            prod*=digit
        return original % (summ+prod)==0

            

        