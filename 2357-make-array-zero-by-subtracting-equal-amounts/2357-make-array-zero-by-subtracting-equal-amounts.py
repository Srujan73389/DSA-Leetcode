class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        unique=[]
        for n in nums:
            if n>0 and n not in unique:
                unique.append(n)
        return len(unique)

        