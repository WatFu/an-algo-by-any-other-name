import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        h = defaultdict(list)
        res = {}
        
        for i, num in enumerate(nums):
            if num in h:
                for a_pair in h[num]:
                    answer = a_pair + [num]
                    answer.sort()
                    tup_answer = tuple(answer)
                    if not tup_answer in res:
                        res[tup_answer] = 1
            for j in range(i):
                curr_pair = [nums[j], num]
                complement = -num-nums[j]
                if not complement in h or (h[complement] != [curr_pair[0], curr_pair[1]] and h[complement] != [curr_pair[1], curr_pair[0]]):
                    h[complement].append(curr_pair)
        
        return list(res.keys())
        
#         h = defaultdict(list)
#         res = {}
        
#         all_products = [[a, b] for a in nums for b in nums]
#         for prod in all_products:
#             diff = -a-b
#             if diff in h:
#                 if h[diff] == [prod[0], prod[1]] or h[diff] == [prod[1], prod[0]]:
#                     continue
#                 else:
#                     h[diff].append(prod)
#             h[diff].append(prod)
        
#         for num in nums:
#             if num in h:
#                 for possible_pair in h:
#                     if 
        
#         return list(res.keys())
