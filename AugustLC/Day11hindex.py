class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        l = len(citations)
        res = 0
        
        for i, cits in enumerate(citations):
            tmp = min(l - i, cits)
            if tmp > res:
                res = tmp
        
        return res
