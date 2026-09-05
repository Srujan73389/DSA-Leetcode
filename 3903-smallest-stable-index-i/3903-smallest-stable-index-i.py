class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_values=[0]*n
        min_values[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            min_values[i]=min(nums[i],min_values[i+1])
        max_value=nums[0]
        for i in range(len(nums)):
            if nums[i]>max_value:
                max_value=nums[i]
           
            if max_value-min_values[i]<=k:
                    return i
        return -1
        