class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        place = 0
        
        for i in range(len(s) - 1, -1, -1):
            res += (ord(s[i]) - 64) * (26 ** place)
            place += 1
        
        return res
