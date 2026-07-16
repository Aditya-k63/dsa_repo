# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt=0
        def value_sum(node):
            if node is None:
                return 0
            left_sum=value_sum(node.left)
            right_sum=value_sum(node.right)
            self.total_tilt+=abs(left_sum-right_sum)
            return node.val+left_sum+right_sum
        value_sum(root)
        return self.total_tilt