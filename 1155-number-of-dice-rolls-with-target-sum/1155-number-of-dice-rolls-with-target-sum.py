class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD=10**9+7
        dp=[[0] *(target+1) for _ in range (n+1)]

        dp[0][0]=1

        for i in range (1,n+1):
            for w in range (1,target+1):
                for f in range (1,k+1):
                    if f <=w:
                        dp[i][w]=(dp[i][w]+dp[i-1][w-f])%MOD
        return dp[n][target]