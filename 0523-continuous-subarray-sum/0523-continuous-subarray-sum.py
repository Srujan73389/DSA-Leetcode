class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_m={0:-1}
        prefixsum=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            rem=prefixsum%k
            if rem in hash_m:
                if i-hash_m[rem]>=2:
                    return True
            else:
                hash_m[rem]=i
        return False