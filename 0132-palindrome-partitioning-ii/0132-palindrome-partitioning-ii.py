class Solution:
    def minCut(self, s: str) -> int:
        n =len(s)
        if n<=1:return 0
        dp=[[False] * n for _ in range (n)]
        for i in range (n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i <=2 or dp[i+1][j-1]):
                    dp[i][j]=True
        cuts=[i for i in range(n)]

        for i in range (n):
            for j in range (i+1):
                if dp[j][i]:
                    if j==0:
                        cuts[i]=0
                    else:
                        cuts[i]=min(cuts[i],cuts[j-1]+1)
        return cuts[n-1]      