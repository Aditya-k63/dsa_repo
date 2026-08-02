# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def help(node)->Tuple[int,int]:
            if node is None:
                return (0,0)
            left_rob,left_skip=help(node.left)
            right_rob,right_skip=help(node.right)

            rob_money=node.val+left_skip+right_skip
            skip_money=max(left_rob,left_skip)+max(right_rob,right_skip)
            return (rob_money,skip_money)
        return max(help(root))