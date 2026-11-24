class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            prod=1
            gcd_val=0
            lcm_val=1
            for j in range(i,n):
                prod*=nums[j]
                gcd_val = self.find_gcd(gcd_val, nums[j])
                lcm_val = self.find_lcm(lcm_val, nums[j])
                if(prod==gcd_val*lcm_val):
                    ans=max(ans,j-i+1)
        return ans

    def find_gcd(self, a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a


    def find_lcm(self, a: int, b: int) -> int:
        return (a // self.find_gcd(a, b)) * b



