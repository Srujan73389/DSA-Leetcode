class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a_box=[]
        b_box=[]
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j]==1:
                    a_box.append((i,j))
                if img2[i][j]==1:
                    b_box.append((i,j))
        d={}
        ans=0
        for a_x,a_y in a_box:
            for b_x,b_y in b_box:
                translation=(b_x-a_x,b_y-a_y)
                if translation in d:
                    d[translation]+=1
                else:
                    d[translation]=1
                ans=max(ans,d[translation])
        return ans
        