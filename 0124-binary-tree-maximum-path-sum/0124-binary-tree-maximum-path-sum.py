# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=float('-inf')
        def get_max(node):
            if node is None:
                return 0
            left_gain=max(0,get_max(node.left))

            right_gain=max(0,get_max(node.right))
            current_path_sum=node.val+left_gain+right_gain
            self.max_sum=max(self.max_sum,current_path_sum)
            return node.val+max(left_gain,right_gain)
        get_max(root)
        return self.max_sum
