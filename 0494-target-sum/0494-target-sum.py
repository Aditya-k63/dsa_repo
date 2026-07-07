class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum=sum(nums)
        if abs(target) > total_sum or (target+ total_sum) % 2!=0:
            return 0
        subset_target=(target+total_sum)//2
        dp=[0] * (subset_target+1)
        dp[0]=1
        for num in nums:
            for j in range(subset_target,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[subset_target]