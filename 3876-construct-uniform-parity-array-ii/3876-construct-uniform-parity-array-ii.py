class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini=nums1[0]
        has_odd=False
        for num in nums1:
            if num<mini:
                mini=num
            if num&1:
                has_odd=True
        if mini&1:
            return True
        return not has_odd
        


            


                





        