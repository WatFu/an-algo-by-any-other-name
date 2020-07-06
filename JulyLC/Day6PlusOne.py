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

# JS: 
# var plusOne = function(digits) {
#    return (BigInt(digits.map(n => n.toString()).join('')) + 1n).toString().split('').map(s => parseInt(s))
# };
# interesting note: this JS solution doesn't work with vanilla parseInt bc it is stored as 64 bit int, which has a max value of 6145390195186705000. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt
