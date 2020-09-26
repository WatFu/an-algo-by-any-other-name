class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        res = n * duration
        
        for i in range(1,n):
            res -= max(0, (timeSeries[i - 1] + duration) - timeSeries[i])
        
        return res
