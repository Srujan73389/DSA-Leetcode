class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        re=[]
        for i in range(len(nums)):
            if nums[i]==target:
                re.append(i)
        return re
