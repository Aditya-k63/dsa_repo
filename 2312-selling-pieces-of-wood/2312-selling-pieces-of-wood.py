class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp=[[0] * (n+1) for _ in range(m+1)]

        for h , w, price in prices:
            dp[h][w]=price
        for h in range (1,m+1):
            for w in range (1,n+1):
                for i in range (1,h):
                    dp[h][w]=max(dp[h][w],dp[i][w]+dp[h-i][w])
                for j in range (1,w):
                    dp[h][w]=max(dp[h][w],dp[h][j]+dp[h][w-j])
        return dp[m][n]