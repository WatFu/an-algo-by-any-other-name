class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return sum(map(lambda z : int(z), bin(x ^ y)[2:]))
        return bin(x ^ y)[2:].count('1')
