class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res=[0]*k
        pre=[0]*k
        for num in nums:
            curr=[0]*k
            r=num%k
            curr[r]+=1
            for old in range(k):
                curr[(old*r)%k]+=pre[old]
            pre=curr
            for i in range(k):
                res[i]+=pre[i]
        return res

        