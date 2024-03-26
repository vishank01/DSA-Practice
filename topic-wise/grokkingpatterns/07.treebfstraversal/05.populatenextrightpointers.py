"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/1214539102

    1 (1)
    2 (2)->    3(1)
4(4) -> 5(3) -> 6(2) -> 7(1)

"""
from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root] if root else [])
        stack = []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                stack.append(node)
            prev_node = None
            while stack:
                node = stack.pop()
                node.next = prev_node
                prev_node = node
        return root
                
                

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class SolutionUsingDFS:
    def connect(self, root: 'Node') -> 'Node':
        self.dfs(root)
        return root
    
    ## (1). left child -> right child
    ## (2). right child -> next.left child
    def dfs(self,root):
        if root == None or root.left == None:
            return
        root.left.next = root.right
        if root.next != None: 
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)


class SolutionOptimized:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root] if root else [])
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i!=l-1:
                    #q[0] is the next node in the same level
                    node.next = q[0]
        return root
                
                