class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^A-Za-z0-9]+', '', s)

        l, r = 0, len(clean_s) - 1
        
        while r > l:
            if ord(clean_s[r]) < 58:
                if ord(clean_s[r]) == ord(clean_s[l]):
                    r -= 1
                    l += 1
                else:
                    return False
                
            if ord(clean_s[r]) > 90:
                if ord(clean_s[r]) == ord(clean_s[l]) or ord(clean_s[r]) - 32 == ord(clean_s[l]):
                    r -= 1
                    l += 1
                else:
                    return False
            else:
                if ord(clean_s[r]) == ord(clean_s[l]) or ord(clean_s[r]) + 32 == ord(clean_s[l]):
                    r -= 1
                    l += 1
                else:
                    return False
        
        return True
