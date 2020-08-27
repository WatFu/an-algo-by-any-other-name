class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        #sort by start point
        #run binary search on endpoints to find start index
        self.intervals = intervals
        self.n = len(intervals) - 1
        self.keys = [x[0] for x in sorted(enumerate(self.intervals),key=lambda i:i[1][0])]
        self.intervals.sort()
        print(self.keys)
        
        res = []
        
        for inter in intervals:
            sortedIndex = self.binSearch(inter[1])
            if sortedIndex == -1:
                res.append(-1)
            else:
                res.append(self.keys[self.binSearch(inter[1])])
        return res
        
    def binSearch(self, target):
        lo, hi = 0, self.n
        if target > self.intervals[hi][0]:
            return -1
        
        while lo < hi:
            mid = int((hi + lo) / 2)
            curr = self.intervals[mid][0]
            if target == curr:
                return mid
            if target > curr:
                lo = mid + 1
            else:
                hi = mid
            
        if self.intervals[lo][0] < target:
            return -1
        return lo
