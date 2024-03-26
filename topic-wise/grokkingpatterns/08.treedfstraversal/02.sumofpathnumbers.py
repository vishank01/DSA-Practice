"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/1214786786
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self,root,res=0):
        if root is None: return 0
        res = res*10+root.val
        if root.left is None and root.right is None: return res
        return self.dfs(root.left,res)+self.dfs(root.right,res)

class SolutionBFS:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:                
        q = deque()
        q.append((root, root.val))
        res = 0
        while q:
            length = len(q)
            for _ in range(length):                
                node,num = q.popleft()
                # add to final result if a leaf node
                if not node.left and not node.right:
                    res += num
                else:
                    if node.left:
                        q.append((node.left, num*10+node.left.val))
                    if node.right:
                        q.append((node.right, num*10+node.right.val))
        
        return res