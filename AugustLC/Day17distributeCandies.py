class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        arr = [0] * num_people
        counter = 1
        position = 0
        
        while candies > 0:
            if counter > candies:
                arr[position] += candies
                candies = 0
            else:
                arr[position] += counter
                candies -= counter
            counter += 1
            position += 1
            position = position%num_people
        
        return arr
