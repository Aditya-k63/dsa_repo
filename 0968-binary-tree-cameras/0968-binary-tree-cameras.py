# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras=0

        def dfs(node)-> int:
            if node is None:
                return 2
            left_state=dfs(node.left)
            right_state=dfs(node.right)
            if left_state==0 or right_state==0:
                self.cameras+=1
                return 1
            if left_state==1 or right_state==1:
                return 2
            return 0
        if dfs(root)==0:
            self.cameras+=1
        return self.cameras