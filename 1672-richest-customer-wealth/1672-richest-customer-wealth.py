class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth=0
        for i in range(len(accounts)):
            summ=sum(accounts[i])
            max_wealth=max(summ,max_wealth)
        return max_wealth
        