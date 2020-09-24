class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h = {}
        
        for letter in s:
            if letter in h:
                h[letter] += 1
            else:
                h[letter] = 1
        
        for letter in t:
            if letter in h:
                h[letter] -= 1
                if h[letter] == -1:
                    return letter
            else:
                return letter
            
