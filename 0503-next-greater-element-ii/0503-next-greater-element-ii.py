class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N=len(nums)
        stack=[]
        ans=[-1]*N

        for i in range(2*N):
            real_idx=i%N

            while stack and nums[stack[-1]]<nums[real_idx]:
                top_idx=stack.pop()
                ans[top_idx]=nums[real_idx]

            if i < N:
                stack.append(real_idx)

        return ans 