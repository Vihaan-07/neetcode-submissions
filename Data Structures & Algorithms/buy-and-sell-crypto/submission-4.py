class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]

        for i in range(len(prices)):
            low = min(low, prices[i])
            p = prices[i] - low
            profit = max(p, profit)

        return profit
            

        