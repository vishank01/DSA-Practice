"""

"""
from collections import deque

def hasPathSum1(self,root,target):
    res = []
    self.dfs(root,target)
    return any(res)
    
def dfs(self, root, target):
    if root is None: return False
    #only when you are at leaf, target should be zero as per question
    if root.left is None and root.right is None and root.val==target: return True
    return self.dfs(root.left, target-root.val) or self.dfs(root.right, target-root.val)

# DFS with stack
def dfsWithStack(self, root, sum):
    if not root: return False
    stack = [(root,root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == sum: return True
        if curr.right: stack.append((curr.right, val+curr.right.val))
        if curr.left: stack.append((curr.left, val+curr.left.val))
    return False
    
# BFS with queue
def hasPathSum(self, root, targetSum):
    d = deque([(root,targetSum-root.val)] if root else [])
    while d:
        node,val = d.popleft()
        #only when you are at leaf, target should be zero as per question
        if node.left is None and node.right is None and val==0: return True
        if node.left: d.append((node.left,val-node.left.val))
        if node.right: d.append((node.right,val-node.right.val))
    return False