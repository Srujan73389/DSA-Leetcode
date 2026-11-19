class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        new=set(friends)
        res=[]
        for i in order:
            if i in new:
                res.append(i)
        return res

        

        