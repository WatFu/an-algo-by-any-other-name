class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        h = {}
        
        for num in nums:
            if num in h:
                res.append(num)
            else:
                h[num] = 1
        
        return res
