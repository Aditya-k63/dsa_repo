class Solution:
    def trap(self, height: List[int]) -> int:
        stack =[]

        water=0

        for i , h_curr in enumerate(height):

            while stack and h_curr > height[stack[-1]]:
                floor_idx=stack.pop()

                if not stack :
                    break 
                left_idx=stack[-1]

                h_layer=min(height[left_idx],h_curr)-height[floor_idx]

                w_layer=i-left_idx-1

                water+=h_layer*w_layer
            stack.append(i)
        return water