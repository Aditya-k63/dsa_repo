class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m,n=len(matrix),len(matrix[0])

        dp=[[0] * n for _ in range (m)]
        max_side=0

        for i in range (m):
            for j in range (n):
                if matrix [i][j]=="1":
                    if i ==0 or j ==0:
                        dp[i][j]=1
                    else:
                        top=dp[i-1][j]
                        left=dp[i][j-1]
                        top_left=dp[i-1][j-1]
                        dp[i][j]=min(top,left,top_left)+1
                    max_side=max(max_side,dp[i][j])
        return max_side*max_side

