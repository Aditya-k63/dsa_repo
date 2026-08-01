# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_zigzag=0
        def dfs(node):
            if node is None:
                return (-1,-1)
            left_left,left_right=dfs(node.left)
            right_left,right_right=dfs(node.right)
            curr_left=1+left_right
            curr_right=1+right_left
            self.max_zigzag=max(self.max_zigzag,curr_left,curr_right)
            return curr_left,curr_right
        dfs(root)
        return self.max_zigzag