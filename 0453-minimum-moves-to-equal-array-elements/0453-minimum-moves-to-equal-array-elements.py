class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves=0
        minimum=min(nums)
        for num in nums:
            moves+=num-minimum
        return moves
        