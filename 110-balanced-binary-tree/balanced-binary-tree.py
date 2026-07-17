# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            leftSubtree = dfs(node.left)
            if(leftSubtree is False):
                return False
            rightSubtree = dfs(node.right)
            if(rightSubtree is False):
                return False
            if(abs(leftSubtree - rightSubtree)> 1):
                return False
            return 1+ max(leftSubtree, rightSubtree)
        if dfs(root) != False:
            return True
        if(not root):
            return True
        return False   