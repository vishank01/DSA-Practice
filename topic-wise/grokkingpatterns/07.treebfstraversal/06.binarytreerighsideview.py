"""

"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root] if root else [])
        out = []
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i==l-1:
                    out.append(node.val)
        return out