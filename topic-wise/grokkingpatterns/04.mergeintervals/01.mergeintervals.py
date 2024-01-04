"""
https://leetcode.com/problems/merge-intervals/submissions/1134863331
https://leetcode.com/problems/merge-intervals/solutions/21452/Share-my-interval-tree-solution-no-sorting

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    n = len(intervals)
    if n<=1: return intervals
    merged_result = []
    intervals = sorted(intervals,key=lambda x:x[0])
    previous = intervals[0]
    for i in range(1,n):
        current = intervals[i]
        if current[0]<=previous[1]:
            #then these intervals are overlapping
            previous[1] = max(current[1],previous[1])
            #don't append to merged_result until above if condition breaks 
            #as we need to merge all those intervals which overlap
        else:
            merged_result.append(previous)
            previous = current
    merged_result.append(previous)
    return merged_result

class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None

class MergeIntervalsUsingIntervalTree:
    def __init__(self):
        self.root = None
    
    def merge(self,intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals)==0: return []
        
        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)
        
        return self.query(self.root)
    
    
    def add(self,node:TreeNode|None,start:int, end:int):     
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)
        
        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)
        
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)
    
    def query(self,node:TreeNode|None):
        if node is None: return []
        
        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []
        
        inserted = False
        
        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
        
        if not inserted:
            res.append([node.start, node.end])
        
        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)
        
        return res
    
if __name__=="__main__":
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(MergeIntervalsUsingIntervalTree().merge([[1,3],[2,6],[8,10],[15,18]]))