class Solution(object):
    def productExceptSelf(self, nums):

        n=len(nums)
        prod=[1]*n
        for i in range(1,n):
            prod[i]=prod[i-1]*nums[i-1]
        right=nums[-1]
        for j in range(n-2,-1,-1):
            prod[j]=prod[j]*right
            right=right*nums[j]
        return prod

        