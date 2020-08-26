class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #cut off for 7 is just costs[1]/costs[0], cut off for 30 is costs[2]/costs[1] * (30/7)
        #should be sliding window problem
        #put all days in a hashmap
        #iterate through days[-1]
        #have running count
        
#         res = [0, 0, 0]
        
#         cutoff7 = int(costs[1]/costs[0])
#         cutoff30 = costs[2]/costs[1] 
        
        
#         return res[0] * costs[0] + res[1] * costs[1] + res[2] * costs[2]

        h = {}
        end = days[-1] + 1
        for day in days:
            h[day] = 1
        
        dp = [0 for _ in range(end)]
        
        for i in range(end):
            if not i in h:
                dp[i] = dp[i - 1]
            else:
                one_index = max(0, i - 1)
                seven_index = max(0, i - 7)
                thirty_index = max(0, i - 30)
                dp[i] = min(dp[one_index] + costs[0], dp[seven_index] + costs[1], dp[thirty_index] + costs[2])
        
        return dp[-1]
