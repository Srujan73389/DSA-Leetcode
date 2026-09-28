class Solution:
    def maxDepth(self, s: str) -> int:
        max_brac=0
        curr_brac=0
        for i in s:
            if i=='(':
                curr_brac+=1
            max_brac=max(curr_brac,max_brac)
            if i==')':
                curr_brac-=1
        return max_brac

        