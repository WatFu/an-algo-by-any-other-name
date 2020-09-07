class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        h = {}
        rev = {}
        
        if not pattern and not string:
            return True

        words = string.split(' ')
        
        if len(pattern) != len(words):
            return False
        
        for i, letter in enumerate(pattern):
            if letter in h or words[i] in rev:
                if not letter in h or h[letter] != words[i] or not words[i] in rev or rev[words[i]] != letter:
                    return False
            else:
                h[letter] = words[i]
                rev[words[i]] = letter
        
        return True
