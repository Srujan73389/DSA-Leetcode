class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res=[0]*k
        prev=[0]*k
        for num in nums:
            curr=[0]*k
            r=num%k
            curr[r]+=1
            for old in range(k):
                curr[(old*r)%k]+=prev[old]
            prev=curr
            for i in range(k):
                res[i]+=prev[i]
        return res