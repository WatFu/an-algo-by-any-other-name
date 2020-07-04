class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 0
        count_sum = 0
        while count_sum < n:
            counter += 1
            count_sum += counter
        
        if count_sum == n:
            return counter
        
        return counter - 1
