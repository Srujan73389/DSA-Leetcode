class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        res=0
        maxl,maxr=height[l],height[r]
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(maxl,height[l])
                res+=maxl-height[l]
            else:
                r-=1
                maxr=max(maxr,height[r])
                res+=maxr-height[r]
        return res



        