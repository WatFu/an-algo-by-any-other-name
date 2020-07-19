class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]
        ap = len(a) - 1
        bp = len(b) - 1
        carry = 0
        res = ''
        
        while ap > -1 or bp > -1:
            print(res, ap, bp)
            if ap > -1 and bp > -1:
                tmp = int(a[ap]) + int(b[bp]) + carry
                if tmp == 1 or tmp == 0:
                    carry = 0
                    res = str(tmp) + res
                else:
                    carry = 1
                    res = str(tmp%2) + res
            elif ap <= -1:
                tmp = int(b[bp]) + carry
                if tmp == 2:
                    carry = 1
                    res = str(0) + res
                else:
                    carry = 0
                    res = str(tmp) + res
            elif bp <= -1:
                tmp = int(a[ap]) + carry
                if tmp == 2:
                    carry = 1
                    res = str(0) + res
                else:
                    carry = 0
                    res = str(tmp) + res

            ap -= 1
            bp -= 1
            
        if carry:
            res = '1' + res
            carry = 0
            
        return res
