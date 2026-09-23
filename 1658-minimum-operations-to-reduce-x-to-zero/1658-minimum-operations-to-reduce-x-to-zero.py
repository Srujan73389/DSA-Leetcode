class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        total=sum(nums)
        target=total-x

        if target < 0:
            return -1
        if target == 0:
            return n
        mp={0:-1}
        max_len=-1
        prefix_sum=0
        for i,num in enumerate(nums):
            prefix_sum+=num
            required=prefix_sum-target
            if required in mp:
                max_len=max(max_len,i-mp[required])
            if prefix_sum not in mp:
                mp[prefix_sum]=i
        if max_len==-1:
            return -1
        return n-max_len

        