class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_m={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff in hash_m:
                return [hash_m[diff]+1,i+1]
            else:
                hash_m[numbers[i]]=i
        
        