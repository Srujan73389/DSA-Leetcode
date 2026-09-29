class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        odd_count=0
        for i in range(len(arr)):
            if arr[i]%2!=0:
                odd_count+=1
                if odd_count==3:
                    return True
            elif arr[i]%2==0:
                odd_count=0
        return False
            
            