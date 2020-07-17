class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use python counter but thats cheating
        h = {}
        res = []
        
        for num in nums:
            if num in h:
                h[num] += 1
            else :
                h[num] = 1
        
        for item in h.items():
            res.append(item)
        
        res.sort(reverse=True, key=lambda x:x[1])
        return list(map(lambda x:x[0], res[0:k]))
