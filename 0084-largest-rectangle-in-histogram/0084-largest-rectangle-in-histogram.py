class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        max_area=0

        height=heights+[0]

        for i in range (len(height)):
            while stack and height[stack[-1]]> height[i]:
                popped_index=stack.pop()
                h=height[popped_index]

                if not stack:
                    w=i
                else:
                    w=i-stack[-1]-1
                max_area=max(max_area,h*w)
            stack.append(i)
        return max_area