class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == node.val:
                result += 1

            return subtree_sum, subtree_count

        dfs(root)

        return result