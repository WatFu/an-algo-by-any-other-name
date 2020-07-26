class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else 1 + (num - 1)%9
