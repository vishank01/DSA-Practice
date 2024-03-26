# Definition for a binary tree node.
"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/1214502575
"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root] if root else [])
        level = 0
        break_ = False
        while q:
            level+=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                #this is leaf node
                if node.left is None and node.right is None:
                    break_ = True
            if break_: break
        return level


        

