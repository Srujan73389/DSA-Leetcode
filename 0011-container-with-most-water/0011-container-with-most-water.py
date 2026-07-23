class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi,l,h=0,0,len(height)-1
        while l<h:
            area=(h-l)*min(height[l],height[h])
            maxi=max(maxi,area)
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return maxi
        