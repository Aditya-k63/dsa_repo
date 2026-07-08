class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days=set(days)
        max_day=days[-1]

        dp=[0]*(max_day +1)

        for i in range (1,max_day+1):
            if i not in travel_days:
                dp[i]=dp[i-1]
            else:
                opt1=dp[i-1]+costs[0]
                opt7=dp[max(0,i-7)]+ costs[1]
                opt30=dp[max(0,i-30)]+costs[2]

                dp[i]=min(opt1,opt7,opt30)
        return dp[max_day]