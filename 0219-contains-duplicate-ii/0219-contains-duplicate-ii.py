class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_m={}
        for i in range(len(nums)):
            if nums[i] in hash_m and i-hash_m[nums[i]]<=k:
                return True
            hash_m[nums[i]]=i
        return False
            
        
        