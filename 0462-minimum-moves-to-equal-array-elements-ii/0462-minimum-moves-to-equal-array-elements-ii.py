class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        moves=0
        median=nums[len(nums)//2]
        for num in nums:
            moves+=abs(num-median)
        return moves

        