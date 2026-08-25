class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        conv_t=set(nums)
        i=k
        while i in conv_t:
            i+=k
            
        return i
        