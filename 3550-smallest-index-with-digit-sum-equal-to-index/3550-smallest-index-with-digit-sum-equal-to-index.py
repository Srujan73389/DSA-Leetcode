class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            val=nums[i]
            tot=0
            while val>0:
                digit=val%10
                tot+=digit
                val//=10
            if tot==i:
                    return i
        return -1

        

        