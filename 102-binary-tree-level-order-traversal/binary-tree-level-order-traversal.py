# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        Q = deque([root])
        ans = []
        if not root:
            return []
        while len(Q)!=0:
            cur = len(Q)
            temp = []
            for i in range(cur):
                node = Q.popleft()
                temp.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            ans.append(temp)
        return ans