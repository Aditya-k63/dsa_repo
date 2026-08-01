# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter=0
        def get_height(node):
            if node is None:
                return 0
            left_h=get_height(node.left)
            right_h=get_height(node.right)
            self.maxdiameter=max(self.maxdiameter,left_h+right_h)
            return 1+max(left_h,right_h)
        get_height(root)
        return self.maxdiameter