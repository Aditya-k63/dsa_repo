# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev=None
        def reverse_postorder(node):
            if node is None :
                return
            reverse_postorder(node.right)
            reverse_postorder(node.left)
            node.right = self.prev
            node.left = None
            self.prev=node
        reverse_postorder(root)
        