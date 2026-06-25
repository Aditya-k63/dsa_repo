class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        
        cols=len(matrix[0])
        heights=[0]*cols
        max_area=0

        for row in matrix :
            for col in range (cols):
                heights[col]=heights[col]+1 if row[col]=="1" else 0
            
            stack =[]

            for i ,h_curr in enumerate (heights+[0]):
                while stack and heights[stack[-1]]>h_curr:
                    h=heights[stack.pop()]
                    w=i if not stack else i -stack[-1]-1
                    max_area=max(max_area,h*w)
                stack.append(i)
        return max_area
        