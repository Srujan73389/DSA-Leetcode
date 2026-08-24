class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=right=0
        max_len=0
        cnt={}
        while right<len(fruits):
            cnt[fruits[right]]=right
            if len(cnt)>2:
                min_val=min(cnt.values())
                del cnt[fruits[min_val]]
                left=min_val+1
            max_len=max(max_len,right-left+1)
            right+=1
        return max_len
        