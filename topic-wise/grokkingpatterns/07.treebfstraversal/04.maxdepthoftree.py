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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        d = deque([root] if root else [])
        while d:
            level+=1
            l = len(d)
            for _ in range(len(d)):
                node = d.popleft()
                if node.left: d.append(node.left)
                if node.right: d.append(node.right)
        return level

