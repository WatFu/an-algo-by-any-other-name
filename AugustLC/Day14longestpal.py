class Solution:
    def longestPalindrome(self, s: str) -> int:
        h = {}
        
        for letter in s:
            if not letter in h:
                h[letter] = 1
            else:
                h[letter] += 1
        
        flag = False
        res = 0
        
        for key in list(h.keys()):
            print(key, h[key])
            if h[key]%2 == 0:
                res += h[key]
            else:
                res += (h[key] - 1)
                flag = True
        
        return res + int(flag)
