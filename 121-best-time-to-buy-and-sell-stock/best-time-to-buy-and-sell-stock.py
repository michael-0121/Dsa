class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0

        for i in range (1, len (prices)):
            temp_profit = prices[i]- min
            if temp_profit > profit:
                profit = temp_profit 
            if prices[i] < min:
                min = prices[i]
        return profit
        