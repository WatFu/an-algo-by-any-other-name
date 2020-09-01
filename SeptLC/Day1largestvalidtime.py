class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def isValidTime(hour, minute):
            return hour > -1 and hour < 24 and minute > -1 and minute < 60
        
        def getPerms(arr):
            res = []
            if len(arr) == 1:
                return [arr]
            for i in range(len(arr)):
                innerRes = getPerms(arr[0:i] + arr[i + 1:])
                for sub in innerRes:
                    res.append([arr[i]] + sub)
            return res
        
        solutions = getPerms(A)
        
        res = []
        
        for sol in solutions:
            h = int(str(sol[0]) + str(sol[1]))
            m = int(str(sol[2]) + str(sol[3]))
            if isValidTime(h, m):
                if not res:
                    res = [h, m]
                else:
                    if h > res[0]:
                        res = [h, m]
                    elif h == res[0] and m > res[1]:
                        res = [h, m]
                        
            
        if not res:
            return ''
        if res[0] < 10:
            hour = "0" + str(res[0])
        else:
            hour = str(res[0])
        if res[1] < 10:
            minute = "0" + str(res[1])
        else:
            minute = str(res[1])
        return hour + ":" + minute
