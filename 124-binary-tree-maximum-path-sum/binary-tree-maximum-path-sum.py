# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            cur_sum = node.val + left_sum + right_sum
            max_sum[0] = max(max_sum[0], cur_sum)
            return node.val + max(left_sum, right_sum)
        max_sum = [float('-inf')]
        dfs(root)
        return max_sum[0]
        
