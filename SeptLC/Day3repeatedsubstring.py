class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        mid = n // 2
        
        for i in range(mid, 0, -1):
            if n%i == 0:
                flag = True
                for j in range(0, n//i - 1):
                    if s[0:i] != s[i*(j+1):i*(j+2)]:
                        flag = False
                        break
                if flag:
                    return flag
        return False
