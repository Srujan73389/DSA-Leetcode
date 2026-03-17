class Solution(object):
    def majorityElement(self, nums):
        ans,count=0,0
        for i in range(len(nums)):
            if (count==0):
                ans=nums[i]
            count+=(1 if ans==nums[i] else -1)
            
        return ans
        