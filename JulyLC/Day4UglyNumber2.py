class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        ugly_numbers = [2,3,4,5]
        two_pointer, three_pointer, five_pointer = 1, 0, 0
        
        while len(ugly_numbers) < n - 1:
            next_num = min(ugly_numbers[two_pointer] * 2, ugly_numbers[three_pointer] * 3, ugly_numbers[five_pointer] * 5)
            if ugly_numbers[two_pointer] * 2 == next_num:
                two_pointer += 1
            if ugly_numbers[three_pointer] * 3 == next_num:
                three_pointer += 1
            if ugly_numbers[five_pointer] * 5 == next_num:
                five_pointer += 1
            ugly_numbers.append(next_num)
            
        return ugly_numbers[n-2] 
