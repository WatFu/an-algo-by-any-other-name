class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        h = {}
        n = len(S)
        
        for i, letter in enumerate(S):
            h[letter] = i
        
        l, r = 0, h[S[0]]
        res = []
        
        while True:
            if l == r:
                res.append(1)
                l += 1
            elif r == n - 1:
                res.append(r - l + 1)
                break
            else:
                first = l
                last = r
                flag = True
                
                while flag:
                    flag = False
                    old_last = last
                    for i in range(first, last + 1):
                        if h[S[i]] > last:
                            flag = True
                        last = max(h[S[i]], last)
                    first = old_last + 1
                res.append(last - l + 1)
            
                l = last + 1
            if l == n:
                break
            r = h[S[l]]
            
        return res
                
