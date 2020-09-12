class Solution:
    def combinationSum3(self, k: int, n: int, low = 1) -> List[List[int]]:
        res = []
        
        if k == 1:
            if n > 0 and n < 10 and n >= low:
                res.append([n])
            return res
        
        for i in range(low,10):
            if n - i >= 1:
                inner_res = self.combinationSum3(k-1, n-i, i + 1)
                for val in inner_res:
                    if val != None:
                        res.append([i] + val)
        
        return res
