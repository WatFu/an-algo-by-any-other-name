class Solution:
    #idea 1: solve for the maxProfit for one pass and remove the subarray for the pass. Counter-example where this wouldn't work: [1,5,1,6,0,0,1]. I would take index 0 to index 3 for profit of 5, and remaining array would be [0,0,1]
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitOne(prices)
    
    def maxProfitOne(self, prices):
        
        max_value = 0
        curr_min = prices[0]
        curr_min_index = 0
        curr_max_index = None
        
        for i, price in enumerate(prices):
            if price < curr_min:
                curr_min = price
                curr_min_index = i
            elif price > curr_min:
                if (price - curr_min) > max_value:
                    max_value = price - curr_min
                    curr_max_index = i
        
        return [max_value, curr_min_index, curr_max_index]
