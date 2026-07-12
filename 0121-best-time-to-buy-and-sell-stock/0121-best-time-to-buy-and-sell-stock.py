class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        free=0
        hold=-float('inf')

        for price in prices:
            hold=max(hold,-price)
            free=max(free,hold+price)

        return free