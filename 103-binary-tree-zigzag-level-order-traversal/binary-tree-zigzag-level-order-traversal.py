# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = True
        if not root:
            return []
        ans = []
        Q = deque([root])
        while Q:
            length = len(Q)
            temp = []
            for i in range(length):
                node = Q.popleft()
                temp.append(node.val)
                if(node.left):
                    Q.append(node.left)
                if(node.right):
                    Q.append(node.right)
            if(flag):
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            flag = not flag
        return ans