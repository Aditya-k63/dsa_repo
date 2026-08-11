class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
            
        # Step 2: Convert to set for O(1) lookup speed
        nums_set = set(nums)
        
        # Step 3: Find the smallest integer missing from nums >= prefix_sum
        ans = prefix_sum
        while ans in nums_set:
            ans += 1
            
        return ans