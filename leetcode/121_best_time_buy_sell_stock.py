class Solution(object):
    def maxProfit(self, prices):
        """
        this method exceed the computational limite
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                p = prices[j] - prices[i]
                if p > max_profit:
                    max_profit = p
        return max_profit

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
