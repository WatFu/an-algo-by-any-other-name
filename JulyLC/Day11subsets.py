class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        h = {}
        res = [[]]
        for i in nums:
            if i in h:
                continue
            else:
                h[i] = 1
                for j in range(len(res)):
                    res.append(res[j] + [i])
                    
        return res
