class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0] *(n+1)
        for i in range (1,n+1):
            current_max=0
            for j in range (1,k+1):
                if i -j >=0:
                    current_max=max(current_max,arr[i-j])
                    option_value = dp[i - j] + (current_max * j)
                    dp[i] = max(dp[i],option_value)
        return dp[n]