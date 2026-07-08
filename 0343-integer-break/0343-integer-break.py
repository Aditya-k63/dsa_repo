class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp=[0] *(n+1)

        dp[1]=1
        dp[2]=1
        for i in range (3,n+1):
            for j in range (1,i):
                product_if_stopped=j*(i-j)
                product_if_continued=j*dp[i-j]
                dp[i]=max(dp[i],product_if_stopped,product_if_continued)
        return dp[n]