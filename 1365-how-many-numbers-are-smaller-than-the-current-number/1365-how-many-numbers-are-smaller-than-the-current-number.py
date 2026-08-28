class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_array=sorted(nums)
        hash_m={}
        ans=[]
        for i in range(len(sorted_array)):
            if sorted_array[i] not in hash_m:
                hash_m[sorted_array[i]]=i
        for i in nums:
            ans.append(hash_m[i])
        return ans
        