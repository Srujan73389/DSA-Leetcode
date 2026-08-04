class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans=[]
        st=set(nums)
        minimum=min(nums)
        maximum=max(nums)
        for i in range(minimum+1,maximum):
            if i not in st:
                ans.append(i)
        return ans

        