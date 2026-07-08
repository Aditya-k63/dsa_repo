class Solution:
    def numSquares(self, n: int) -> int:
        squares=[]

        i =1
        while i* i <=n:
            squares.append(i*i)
            i+=1
        dp=[float("inf")] * (n+1)

        dp[0]=0

        for square in squares:
            for w in range (square,n+1):
                dp[w]=min(dp[w],dp[w-square]+1)
        return dp[n]

