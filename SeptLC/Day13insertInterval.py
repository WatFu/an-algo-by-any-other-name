class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        start, end = -1, -1
        start_val, end_val = -1, -1
        index = 0
        
        n = len(intervals)
        
        while start == -1 and index < n:
            curr = intervals[index]
            if newInterval[0] <= curr[0]:
                start = index
                start_val = newInterval[0]
                break
            elif newInterval[0] <= curr[1]:
                start = index
                start_val = curr[0]
                break
            index += 1
        
        while end == -1 and index < n:
            curr = intervals[index]
            if newInterval[1] < curr[0]:
                end = index - 1
                end_val = newInterval[1]
                break
            elif newInterval[1] == curr[0] or newInterval[1] < curr[1]:
                end = index
                end_val = curr[1]
                break
            index += 1


        if index == n and start == -1:
            return intervals + [newInterval]
        if index == n and end == -1:
            return intervals[:start] + [[start_val, newInterval[1]]]
        return intervals[:start] + [[start_val, end_val]] + intervals[end + 1:]
