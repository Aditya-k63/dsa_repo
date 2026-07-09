class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n=len(s)
        MOD=10**9+7

        dp=[0] *(n+1)

        dp[0]=1

        for i in range(1,n+1):
            for j in range(max(0,i-10),i):
                num_str=s[j:i]
                if num_str[0]=="0":
                    continue
                value=int(num_str)
                if value<=k:
                    dp[i]=(dp[i]+dp[j]) % MOD
        return dp[n]