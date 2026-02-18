class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in ha:
                return [ha[diff],i]
            ha[nums[i]]=i
        
