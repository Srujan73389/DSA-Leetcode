class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        grp=set()
        for n in nums:
            if n in grp:
                grp.remove(n)
            else:
                grp.add(n)
        return len(grp)==0
        