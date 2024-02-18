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

def insert_intervals(intervals:list[list[int]],new_interval:list[int])->list[list[int]]:
    """
        if [a,b] [c,d] are two intervals then, 
            1. To check for overlapping condition b<c provided, intervals are sorted by start times
            2. Once overlapping is achieved, then always this condition is satisifed a<=d
                this condition satisfies 4/6 overlapping cases out of which 2 are completely non overlapping

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
            

if __name__=="__main__":
    print(insert_intervals([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))