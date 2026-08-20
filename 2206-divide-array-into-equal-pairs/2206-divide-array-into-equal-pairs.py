class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt={}
        for n in nums:
            cnt[n]=cnt.get(n,0)+1
        for i in cnt.values():
            if i%2!=0:
                return False
        return True
        