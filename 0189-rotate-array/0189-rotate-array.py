class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        n=len(nums)-1
        l,r=0,n
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=k,n
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

       
        