class Solution:
    def search(self, nums, target):
        if target in set(nums):
            return nums.index(target)
        else:
            return -1