"""
https://leetcode.com/problems/missing-number/submissions/1180698036

Problem Statement:
    We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.

Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Solution:
    This problem follows the Cyclic Sort pattern. Since the input array contains unique numbers from the range 0 to n, 
    we can use a similar strategy as discussed in Cyclic Sort pattern to place the numbers on their correct index. 
    Once we have every number in its correct place, we can iterate the array to find the index which does not have the correct number, and that index will be our missing number.

    However, there are two differences with Cyclic Sort:

    In this problem, the numbers are ranged from 0 to n, compared to 1 to n in the Cyclic Sort. This will make two changes in our algorithm:
        1. Each number should be equal to its index, compared to index - 1 in the Cyclic Sort. 
        2. Therefore => nums[i] == nums[nums[i]]
        3. Since the array will have n numbers, which means array indices will range from 0 to n-1. 
        4. Therefore, we will ignore the number n as we can’t place it in the array, so => nums[i] < nums.length
        5. Say we are at index i. If we swap the number at index i to place it at the correct index, we can still have the wrong number at index i.
        6. This was true in Cyclic Sort too. It didn’t cause any problems in Cyclic Sort as over there, we made sure to place one number at its correct place in each step, but that wouldn't be enough in this problem as we have one extra number due to the larger range.
        7. Therefore, we will not move to the next number after the swap until we have a correct number at the index i.

Cyclic Sort Theory:

    We are given an array containing n objects. Each object, when created, was assigned a unique number from 1 to n based on their creation sequence. 
    This means that the object with sequence number 3 was created just before the object with sequence number 4.

    Problem Statement:
        Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
        For simplicity, let's assume we are passed an integer array containing only the sequence numbers, though each number is actually an object. As we know, the input array contains numbers in the range of 1 to n. We can use this fact to devise an efficient way to sort the numbers. Since all numbers are unique, we can try placing each number at its correct place, i.e., placing 1 at index 0, placing 2 at index 1, and so on.

    Algorithm:
        To place a number (or an object in general) at its correct index, we first need to find that number. 
        If we first find a number and then place it at its correct place, it will take us O(N²), which is not acceptable.
        Instead, what if we iterate the array one number at a time, and if the current number we are iterating is not at the correct index, we swap it with the number at its correct index.
        This way we will go through all numbers and place them in their correct indices, hence, sorting the whole array.
"""

def find_missing_number(nums: list[int]) -> int:
    """
    >>> find_missing_number([3,0,1])
    2
    >>> find_missing_number([9,6,4,2,3,5,7,0,1])
    8
    >>> find_missing_number([0,1])
    2
    """
    i=0
    n = len(nums)
    while i<n:
        correct_idx = nums[i]
        if correct_idx<n and correct_idx!=i:
            nums[correct_idx],nums[i]=nums[i],nums[correct_idx]
        else: i+=1
    for i in range(n):
        if nums[i]!=i: return i
    return i+1

if __name__=="__main__":
    import doctest
    doctest.testmod()