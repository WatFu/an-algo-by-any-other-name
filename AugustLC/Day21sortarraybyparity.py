class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e = []
        o = []
        
        for num in A:
            if num%2 == 0:
                e.append(num)
            else:
                o.append(num)
        
        return e + o
