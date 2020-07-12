class Solution:
    def reverseBits(self, n: int) -> int:
        string = str(bin(n)[2:])
        string = '0' * (32 - len(string)) + string
        return int(string[::-1], 2)
        # for optimization, hash all 
