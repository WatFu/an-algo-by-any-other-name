class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        #sort to get last place into first then rotate all k
        #only concern is that the act of flipping is very expensive, need to update k indexes every time
        
        self.h = {}
        self.rev_h = {}
        res = []
        
        for i, num in enumerate(A):
            self.h[i] = num
            self.rev_h[num] = i
        
        pointer = len(A) - 1
        
        while pointer > 0:
            if self.h[pointer] != pointer + 1:
                curr_pos = self.rev_h[pointer + 1]
                res.append(curr_pos + 1)
                self.rotate(curr_pos)
                res.append(pointer + 1)
                self.rotate(pointer)
            pointer -= 1
        
        return res
    
    def rotate(self, k):
        mid = int(k / 2)
        for i in range(mid + 1):
            front = self.h[i]
            back = self.h[k - i]
            self.h[i], self.h[k - i] = back, front
            self.rev_h[front], self.rev_h[back] = k - i, i
