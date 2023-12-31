"""
https://www.designgurus.io/viewer/document/grokking-the-coding-interview/63ddae8dff57d05f33ad0bc7
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/

Shortest Subarray to be Removed to Make Array Sorted

Problem Statement:
    Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
    Return the length of the shortest subarray to remove. A subarray is a contiguous subsequence of the array.


Example 1:

    Input: arr = [1,2,3,10,4,2,3,5]
    Output: 3
    Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
    Another correct solution is to remove the subarray [3,10,4].

Example 2:

    Input: arr = [5,4,3,2,1]
    Output: 4
    Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:

    Input: arr = [1,2,3]
    Output: 0
    Explanation: The array is already non-decreasing. We do not need to remove any elements.
    

Constraints:

    1 <= arr.length <= 105
    0 <= arr[i] <= 109
"""

def find_len_of_shortest_subarray(nums:list[int])->int:
    """
        we have to remove smallest subarray after which, whole array will be sorted.
            find l and r,
            0 to l is one sorted piece
            r to n-1 is other sorted piece
            we have to keep some elements from 0 to l and check the smallest r that's suitable to hold the left piece.
                edge case1: we may remove all left elements, so answer is r (we have to remove all from 0 to r-1)
                edgecase2: we can remove all right ones (n-l+1)
                edgecase3: what if l==0 and r==n-1
                edgecase3.1: 6,5,4,3,2,1 a[0]<a[n-1], so i must remove i=1 to n-1
                Edgecase3.2: 6,5,13,11 , we can remove all from i=1 to n-2
            so ans=min of all values

        Since we can only remove a subarray, the final remaining elements must be either: (1) solely a prefix, (2) solely a suffix or (3) a merge of the prefix and suffix.

            Find the monotone non-decreasing prefix [a_0 <= ... a_i | ...]
            l is the index such that arr[l+1] < arr[l]
            Find the monotone non-decreasing suffix [... | a_j <= ... a_n]
            r is the index such that arr[r-1] > arr[r]
            Try to "merge 2 sorted arrays", if we can merge, update our minimum to remove.
    
    """
    n = len(nums)
    l, r = 0, n-1
    while l < r and nums[l+1] >= nums[l]:
        l += 1
    if l == n-1:
        return 0 # whole array is sorted
    while r > 0 and nums[r-1] <= nums[r]:
        r -= 1
    
    to_remove = min(len(nums) - l - 1, r) # case (1) and (2)
    
    # case (3): try to merge
    for iL in range(l+1):
        if nums[iL] <= nums[r]:
            to_remove = min(to_remove, r - iL - 1)
        elif r < len(nums) - 1:
            r += 1
        else:
            break
    return to_remove
    
if __name__=="__main__":
    print(find_len_of_shortest_subarray(nums = [1,2,3]))#0
    print(find_len_of_shortest_subarray(nums = [2,1]))#0
    print(find_len_of_shortest_subarray(nums = [2,2,2,1,1,1]))#3
    # print(find_len_of_shortest_subarray(nums = [1,2,3,10,4,2,3,5]))#3
    # print(find_len_of_shortest_subarray(nums = [5,4,3,2,1]))#4