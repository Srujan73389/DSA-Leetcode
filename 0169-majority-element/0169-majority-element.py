class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,res=0,0
        for i in nums:
            if count==0:
                res=i
            count+=(1 if i==res else -1)
        return res        