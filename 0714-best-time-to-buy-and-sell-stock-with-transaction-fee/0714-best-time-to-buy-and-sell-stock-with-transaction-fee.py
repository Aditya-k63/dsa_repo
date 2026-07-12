class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        free=0
        hold=-float('inf')

        for price in prices:
            prev_free=free
            hold=max(hold,free-price)
            free=max(free,hold+price-fee)
        return free