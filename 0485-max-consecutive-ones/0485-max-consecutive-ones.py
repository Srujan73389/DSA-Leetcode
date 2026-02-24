class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c,m=0,0
        for i in nums:
            if i==1:
                c+=1
            else:
                m=max(c,m)
                c=0
        return max(m,c)

        