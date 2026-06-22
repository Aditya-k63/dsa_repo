class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next={}

        for num in nums2:
            while stack and stack[-1] < num:
                popped_num=stack.pop()
                next[popped_num]=num
            stack.append(num)

        ans=[]
        for num in nums1:
            ans.append(next.get(num,-1))
        return ans