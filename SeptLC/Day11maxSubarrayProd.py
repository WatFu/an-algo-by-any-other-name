class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        pos = -math.inf
        neg = -math.inf
        
        for num in nums:
            if num > 0:
                if pos == -math.inf or pos == 0:
                    pos = num
                else:
                    pos *= num
                if neg == -math.inf or neg == 0:
                    neg = num
                else:
                    neg *= num
            elif num < 0:
                if neg == -math.inf or neg == 0:
                    neg = num
                else:
                    neg *= num
                res = max(res, neg, pos)
                pos = -math.inf
            
            else:
                res = max(res, neg, pos)
                pos = 0
                neg = 0
        
        
                
        
        return max(res, pos, neg)
