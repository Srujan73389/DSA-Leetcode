class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        upper=len(candyType)//2
        lower=len(set(candyType))
        return min(upper,lower)
        