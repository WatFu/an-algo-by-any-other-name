class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        h = {}
        
        for num in nums:
            if num in h:
                del h[num]
            else:
                h[num] = 1
        
        return list(h.keys())
