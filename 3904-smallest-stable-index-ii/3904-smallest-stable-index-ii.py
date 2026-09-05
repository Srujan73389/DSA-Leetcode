class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_val=[0]*n
        min_val[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            min_val[i]=min(nums[i],min_val[i+1])
        max_val=nums[0]
        for i in range(len(nums)):
            if nums[i]>max_val:
                max_val=nums[i]
            if max_val-min_val[i]<=k:
                return i
        return -1
        