# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_len=0
        def get_univ_len(node):
            if node is None:
                return 0
            left_len=get_univ_len(node.left)
            right_len=get_univ_len(node.right)
            left_arrow=right_arrow=0
            if node.left and node.left.val==node.val:
                left_arrow=left_len+1
            if node.right and node.right.val==node.val:
                right_arrow=right_len+1
            self.max_len=max(self.max_len,left_arrow+right_arrow)
            return max(left_arrow,right_arrow)
        get_univ_len(root)
        return self.max_len
