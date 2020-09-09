class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        one = version1.split('.')
        two = version2.split('.')
        
        m = len(one)
        n = len(two)
        
        one_pointer, two_pointer = 0, 0
        
        while one_pointer < m or two_pointer < n:
            if one_pointer >= m:
                curr_one = 0
            else:
                curr_one = int(one[one_pointer])
            if two_pointer >= n:
                curr_two = 0
            else:
                curr_two = int(two[two_pointer])
            if curr_one > curr_two:
                return 1
            elif curr_one < curr_two:
                return -1
            one_pointer += 1
            two_pointer += 1
            
        return 0
