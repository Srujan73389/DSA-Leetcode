class Solution(object):
    def trap(self, height):
        left,right=0,len(height)-1
        water=0
        left_m,right_m=height[left],height[right]
        while left <right:
            if left_m <=right_m:
                left+=1
                left_m=max(left_m,height[left])
                water+=left_m-height[left]
            else:
                right-=1
                right_m=max(right_m,height[right])
                water+=right_m-height[right]
        return water

       