# Definition for a binary tree node.
"""https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/solutions/750132/four-python-solutions
"""
from collections import deque
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class SolutionUsingStack:
    #using stack
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return None
        q = deque()
        output = []
        is_odd_level = 1
        q.append(root)
        while q:
            length = len(q)
            stack = []
            elements_in_current_level = []
            for _ in range(length):
                ele = q.popleft()
                if not is_odd_level:
                    stack.append(ele)
                else:
                    elements_in_current_level.append(ele.val)
                if ele.left:  q.append(ele.left)
                if ele.right:  q.append(ele.right)
            #use stack to reverse elements (instead of stack if elements are directly pushed, then reversed() should be used)
            while stack:
                elements_in_current_level.append(stack.pop().val)
            output.append(elements_in_current_level)
            is_odd_level ^=1
        return output
    

class SolutionUsingDequeFunctionality:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return None
        q = deque()
        output = []
        is_odd_level = 1
        q.append(root)
        while q:
            length = len(q)
            elements_in_current_level = []
            for _ in range(length):
                if is_odd_level:
                    #for odd level (1,3,5, ...) it is as usual
                    ele = q.popleft()
                    if ele.left:  q.append(ele.left)
                    if ele.right:  q.append(ele.right)
                else:
                    #for even level, pop from right of queue, and add it's children from left
                    #from right of current node to maintain bfs traversal for next node
                    ele = q.pop()
                    if ele.right:  q.appendleft(ele.right)
                    if ele.left:  q.appendleft(ele.left)
                elements_in_current_level.append(ele.val)
            output.append(elements_in_current_level)
            is_odd_level ^=1
        return output