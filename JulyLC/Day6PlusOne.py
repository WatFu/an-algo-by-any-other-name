class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         if not digits:
#             return []
        
#         pointer = len(digits) - 1
        
#         while pointer > -1:
#             digits[pointer] = digits[pointer] + 1
#             if digits[pointer] == 10:
#                 digits[pointer] = 0
#                 pointer -= 1
#             else:
#                 break
        
#         if digits[0] == 0:
#             return [1] + digits
#         else:
#             return digits
        return list(map(int, list(str(int(''.join(list(map(str, digits)))) + 1))))

# JS: return (parseInt(digits.map(n => n.toString()).join('')) + 1).toString().split('').map(s => parseInt(s))
