class Solution:
    def climbStairs(self, n: int,memo:dict=None) -> int:
        if memo is None :
            memo={}
        if n <=1:
            return 1
        if n in memo :
            return memo[n]
        memo[n]=self.climbStairs(n-1,memo)+self.climbStairs(n-2,memo)
        return memo[n]
