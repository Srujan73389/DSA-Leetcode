class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        total=sum(nums)
        target=total-x
        start=end=0
        max_len=-1
        pref=0
        while end<n:
            pref+=nums[end]
            while pref>target and start <= end:
                pref-=nums[start]
                start+=1
            if pref==target:
                max_len=max(max_len,end-start+1)
            end+=1
        if max_len==-1:
            return -1
        return n-max_len

        
        