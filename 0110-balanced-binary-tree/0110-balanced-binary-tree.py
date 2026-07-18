# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node is None:
                return 0
            left_h=check(node.left)
            right_h=check(node.right)
            if left_h==-1 or right_h==-1 or abs(left_h-right_h)>1:
                return -1
            return max(left_h,right_h)+1
        return check(root) !=-1
        