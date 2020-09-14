class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp1, dp2 = 0, 0
        
        for num in nums:
            curr = max(dp1 + num, dp2)
            dp1, dp2 = dp2, curr
        
        return dp2
