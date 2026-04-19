class Solution(object):
    def maxProfit(self, prices):
        
        profit=0
        buy=prices[0]
        for i in prices:
            if i>buy:
                profit=max(profit,i-buy)
            else:
                buy=i
        return profit