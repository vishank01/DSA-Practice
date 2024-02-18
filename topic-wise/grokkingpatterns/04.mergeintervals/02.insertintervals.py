"""
https://leetcode.com/problems/insert-interval/description/
https://leetcode.com/problems/insert-interval/submissions/1139852376
https://leetcode.com/problems/insert-interval/submissions/1178651505


Problem Statement: 
    Insert Intervals
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
        Return intervals after the insertion.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
    

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
"""
import bisect

def insert_intervals(intervals:list[list[int]],new_interval:list[int])->list[list[int]]:
    """
        if [a,b] [c,d] are two intervals then, 
            1. To check for overlapping condition b<c provided, intervals are sorted by start times
            2. Once overlapping is achieved, then always this condition is satisifed a<=d
                this condition satisfies 4/6 overlapping cases out of which 2 are completely non overlapping
    >>> insert_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
    [[1, 2], [3, 10], [12, 16]]

    >> insert_intervals([[1,5]],[6,8])
    [[1, 5], [6, 8]]

    """
    i=0
    output = []
    n = len(intervals)
    
    while i<n and intervals[i][1] < new_interval[0]:
        output.append(intervals[i]);i+=1
    while i<n and intervals[i][0]<=new_interval[1]:
        new_interval[0] = min(intervals[i][0],new_interval[0])
        new_interval[1] = max(intervals[i][1],new_interval[1])
        i+=1
    output.append(new_interval)
    while i<n:
        output.append(intervals[i]);i+=1
    return output
            
def insert_intervals_binary_search(intervals:list[list[int]],new_interval:list[int])->list[list[int]]:
    """
        Use binary search twice to find the overlapping intervals.
        . bisect_left searches the leftmost interval whose end is greater than new interval's start. 
        . bisect_right searches the rightmost interval whose start is less than the new interval's end. 

        if nums = [1,3,5,7,10,25,25,49,55] and 25 to be inserted,then 
            bisect_right gives index 7
            bisect_left gives index 5
        
        Note that the right bound right_idx returned by bisect_right is not inclusive. 
        Thus, if right_idx - left_idx <= 0, then there's no interval overlapped with the new one. 
        Otherwise, there are at least one overlapping intervals, and we can merge them in O(1) complexity.

        The bisect_left and bisect_right functions in Python's bisect module return sthe same index when the searched element is not present in the list.
        They differ when the searched element is present in the list. bisect_left returns the leftmost index where the element can be inserted without changing the order of elements, 
        while bisect_right returns the rightmost index where the element can be inserted without changing the order of elements.

    >>> insert_intervals_binary_search([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
    [[1, 2], [3, 10], [12, 16]]

    >> insert_intervals_binary_search([[1,5]],[6,8])
    [[1, 5], [6, 8]]
    """
    # intervals < left_idx does not overlap
    left_idx = bisect.bisect_left(intervals,new_interval[0],key=lambda x:x[1])
    right_idx = bisect.bisect_right(intervals,new_interval[1],key=lambda x:x[0])
    # merge new interval with intervals[left_idx:right_idx]
    if right_idx!=left_idx:
        new_start = min(new_interval[0], intervals[left_idx][0])
        new_end = max(new_interval[1], intervals[right_idx-1][1])
    else:
        new_start,new_end = new_interval
    return intervals[:left_idx]+[[new_start,new_end]]+intervals[right_idx:]

if __name__=="__main__":
    import doctest
    doctest.testmod()