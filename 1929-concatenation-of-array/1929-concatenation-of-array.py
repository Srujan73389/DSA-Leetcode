class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for m in range(2):
            for i in nums:
                ans.append(i)
        return ans
        
        