class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = {}
        g = {}
        
        bull = 0
        cow = 0
        
        for i, letter in enumerate(guess):
            sec_letter = secret[i]
            if letter == sec_letter:
                bull += 1
            else:
                if sec_letter in h:
                    h[sec_letter] += 1
                else:
                    h[sec_letter] = 1
                if letter in g:
                    g[letter] += 1
                else:
                    g[letter] = 1
                    
        for val in list(g.items()):
            key = val[0]
            num = val[1]
            
            if key in h:
                sec_val = h[key]
            else:
                sec_val = 0
            
            cow += min(sec_val, num)
            
        return str(bull) + 'A' + str(cow) + 'B'
