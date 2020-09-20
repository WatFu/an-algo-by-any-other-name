class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        minDig = int(math.log10(low))
        maxDig = int(math.log10(high))
        res = []
        
        while minDig < maxDig + 1 and minDig <= 8:
            for i in range(1,10):
                num = i
                for j in range(1,minDig + 1):
                    num *= 10
                    num += i + j
                if num <= high:
                    if num >= low:
                        res.append(num)
                    if num%10 == 9:
                        break
                else:
                    break
            minDig += 1
        
        return res
                    
                    
