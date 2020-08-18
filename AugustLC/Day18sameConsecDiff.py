class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        h = {}
        
        for i in range(10):
            h[str(i)] = 1
        
        if N == 1:
            return list(h.keys())
        
        while N > 1:
            tmp_dict = h.copy()
            for el in list(tmp_dict.keys()):
                curr_dig = int(el[-1])
                del h[el]
                if len(el) == 1 and el == '0':
                    continue
                if curr_dig - K > -1:
                    h[el + str(curr_dig - K)] = 1
                if curr_dig + K < 10:
                    h[el + str(curr_dig + K)] = 1
            N -= 1
        
        return list(h.keys())
