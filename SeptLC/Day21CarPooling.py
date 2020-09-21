class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        starts = {}
        ends = {}
        last = trips[0][2]
        
        for trip in trips:
            if trip[1] in starts:
                starts[trip[1]] += trip[0]
            else:
                starts[trip[1]] = trip[0]
            if trip[2] in ends:
                ends[trip[2]] += trip[0]
            else:
                ends[trip[2]] = trip[0]
            last = max(last, trip[2])
        
        curr = 0
            
        for i in range(last + 1):
            if i in starts:
                curr += starts[i]
            if i in ends:
                curr -= ends[i]
            if curr > capacity:
                return False
        
        return True
        
