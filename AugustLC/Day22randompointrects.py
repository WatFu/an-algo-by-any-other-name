import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.count = len(self.rects)
        self.weights = [0] * self.count
        
        self.weights[0] = self.area(rects[0])
        
        for i in range(1,self.count):
            self.weights[i] += self.weights[i - 1] + self.area(self.rects[i])
        
    
    def area(self, coordinates):
        return (coordinates[2] - coordinates[0] + 1) * (coordinates[3] - coordinates[1] + 1)

    def pick(self) -> List[int]:
        searchval = random.randint(0, self.weights[-1])
        

        l, r = 0, self.count - 1
        
        while l < r:
            mid = (r + l) // 2
            if searchval <= self.weights[mid]:
                r = mid
            else:
                l = mid + 1
        
        rect_coords = self.rects[l]
        
        return [random.randint(rect_coords[0], rect_coords[2]), random.randint(rect_coords[1], rect_coords[3])]
