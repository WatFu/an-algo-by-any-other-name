class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        
        if not prices:
            return res
        
        low = prices[0]
        
        n = len(prices)
        
        for i in range(1,n):
            if prices[i] < low:
                low = prices[i]
            else:
                res = max(res, prices[i] - low)
        
        return res
