class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1 or len(word) == 0:
            return True
        
        if ord(word[0]) >= 97:
            for i in range(1,len(word)):
                if (ord(word[i])) < 97:
                    return False
            return True
        
        if ord(word[1]) >= 97:
            for i in range(2,len(word)):
                if (ord(word[i])) < 97:
                    return False
            return True
        
        for i in range(2,len(word)):
            if (ord(word[i])) >= 97:
                return False
        return True
