class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        curr=nums[0]
        res=curr
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                curr+=nums[i]
            else:
                curr=nums[i]
            res=max(curr,res)
        return res
        