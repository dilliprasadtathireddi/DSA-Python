# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q = deque([root])
        ans = []
        while Q:
            length = len(Q)
            temp = []
            for i in range(length):
                node = Q.popleft()
                if(node.left):
                    Q.append(node.left)
                if(node.right):
                    Q.append(node.right)
                temp.append(node.val)
            ans.append(temp)

        return ans


