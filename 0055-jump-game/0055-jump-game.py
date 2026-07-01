class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        max_r =0
        for i in range (n):
            if i > max_r:
                return False
            max_r= max(max_r,i+nums[i])

            if max_r >=n-1:
                return True 
        return max_r>=n-1