class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=0
        counts=0
        for num in nums:
            if counts==0:
                element=num
            counts+=1 if num==element else -1
        return element
        