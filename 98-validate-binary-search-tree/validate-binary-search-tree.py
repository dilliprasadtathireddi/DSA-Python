# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, start, end):
            if not root:
                return True
            if root.val >= end or root.val <= start:
                return False
            left = helper(root.left, start, root.val)
            right = helper(root.right, root.val, end)
            return left and right
        ans= helper(root, float('-inf'), float('inf'))
        return ans