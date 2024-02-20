"""
https://leetcode.com/problems/first-missing-positive/submissions/1180820386?source=submission-noac

Problem Statement First Missing Positive:
    Given an unsorted integer array nums, return the smallest missing positive integer.
    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.

Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

Solution:
    This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number with one big difference. 
    1. In this problem, the numbers are not bound by any range so we can have any number in the input array.
    2. We will follow a similar approach though as discussed in Find the Missing Number to place the numbers on their correct indices 
    3. Ignore all numbers that are out of the range of the array (i.e., all negative numbers and all numbers greater than or equal to the length of the array). 
    4. Once we are done with the Cyclic Sort we will iterate the array and the first index that does not have the correct number will be the smallest missing positive number!

"""
def first_missing_positive(nums: list[int]) -> int:
    """
    >>> first_missing_positive([3,4,-1,1])
    2
    >>> first_missing_positive([1,2,0])
    3
    >>> first_missing_positive([7,8,9,11,12])
    1
    """
    i = 0
    n = len(nums)
    while i < n:
        # put all >0 numbers starting from index 1
        correct_idx = nums[i]-1
        if (
            correct_idx < n
            and nums[i] > 0
            and nums[correct_idx] != nums[i]
        ):
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i]-1 != i:
            return i+1
    return n+1


if __name__=="__main__":
    import doctest
    doctest.testmod()