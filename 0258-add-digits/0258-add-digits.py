class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            summ=0
            while num>0:
                digit=num%10
                num//=10
                summ+=digit
            num=summ
        return num
        