class Solution(object):
    def maxProfit(self, prices):
        """
        We should buy and sell stock as long as the price on the
        second day is larger than previous day
        """
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit