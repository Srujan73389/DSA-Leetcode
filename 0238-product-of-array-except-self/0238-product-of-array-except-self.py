class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[1]*len(nums)
        for i in range(1,len(nums)):
            prod[i]=prod[i-1]*nums[i-1]
        right=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            prod[i]*=right
            right*=nums[i]
        return prod        