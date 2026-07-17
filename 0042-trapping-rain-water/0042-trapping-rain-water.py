class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        left_m=height[l]
        right_m=height[r]
        res=0
        while l<r:
            if left_m<right_m:
                l+=1
                left_m=max(left_m,height[l])
                res+=left_m-height[l]
            else:
                r-=1
                right_m=max(right_m,height[r])
                res+=right_m-height[r]
        return res
        