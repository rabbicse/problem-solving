class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        ans = 0
        
        for i in range(len(prices) - 1):
            result = prices[i + 1] - prices[i]
            if result > 0:
                ans += result
        
        return ans
