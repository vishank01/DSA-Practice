"""
https://leetcode.com/problems/kth-missing-positive-number/submissions/1180847018

Problem Statement:
    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
    Return the kth positive integer that is missing from this array.

Example 1:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
    Input: arr = [1,2,3,4], k = 2
    Output: 6
    Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length

"""
from collections import Counter

def find_kth_positive_missing_number_using_hash(nums: list[int],k:int) -> int:
    """
    >>> find_kth_positive_missing_number_using_hash([2,3,4,7,11],5)
    9
    >>> find_kth_positive_missing_number_using_hash([1,2,3,4],2)
    6
    """
    i = 1;j=1
    counter = Counter(nums)
    while j<=k:
        while counter.get(i,0)>0:
            i+=1
        i+=1;j+=1
    return i-1


if __name__=="__main__":
    import doctest
    doctest.testmod()