class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ar1=set(nums1)
        ar2=set(nums2)
        res=[]
        for i in ar2:
            if i in ar1:
                res.append(i)
        return res

        
        