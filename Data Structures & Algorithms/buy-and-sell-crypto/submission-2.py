class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L, R = 0, 1 #Left for buying // Right for Selling

        while R < len(prices):
            # Profitable ?
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1
        return maxProfit
        
        
        