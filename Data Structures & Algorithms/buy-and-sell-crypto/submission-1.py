class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        L, R = 0, 1 #Left for buying // Right for Selling

        for i in range(len(prices) - 1):
            
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)
        
            if prices[L] > prices[R]:
                L = R
                R += 1
            else:
                R += 1
        
        return maxProfit
        
        
        