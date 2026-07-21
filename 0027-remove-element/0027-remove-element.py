class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for valu in range(len(nums)):
            if nums[valu]!=val:
                nums[i]=nums[valu]
                i+=1
        return i
        