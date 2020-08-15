class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[1])
        
        n, count, end = len(intervals), 0, intervals[0][1]
        
        for i in range(1,n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1
        
        return count
            
