class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prod=[1]*n
        for i in range(1,n):
            prod[i]=prod[i-1]*nums[i-1]
        right=nums[-1]
        for j in range(n-2,-1,-1):
            prod[j]*=right
            right*=nums[j]
        return prod
        