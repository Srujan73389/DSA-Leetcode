class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        min_val=float('inf')
        sum=0
        for right in range(len(nums)):
            sum+=nums[right]
            while (sum>=target):
                min_val=min(min_val,right-left+1)
                sum-=nums[left]
                left+=1
        return 0 if min_val==float('inf') else min_val

       
        