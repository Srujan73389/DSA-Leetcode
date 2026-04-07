class Solution(object):
    def containsDuplicate(self, nums):
        has=set()
        for i in nums:
            if i in has:
                return True
            has.add(i)
        return False
        
        