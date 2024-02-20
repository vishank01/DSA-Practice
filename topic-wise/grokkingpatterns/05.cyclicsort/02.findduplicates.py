"""
https://leetcode.com/problems/find-the-duplicate-number/submissions/1180758203
Problem Statement: Find the Duplicate Number
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Constraints:
    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""
def find_duplicate(nums: list[int]) -> int:
    """
    >>> find_duplicate([1,3,4,2,2])
    2
    >>> find_duplicate([3,1,3,4,2])
    3
    """
    i = 0
    n = len(nums)
    while i<n:
        if nums[i]-1<n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        else: i+=1
    for i in range(n):
        if nums[i]!=i+1: return nums[i]
    return 0

def find_all_duplicates(nums:list[int])->list[int]:
    """
    >>> find_all_duplicates([4,3,2,7,8,2,3,1])
    {2, 3}
    >>> find_all_duplicates([1,1,2])
    {1}
    """
    i = 0
    res = set()
    n = len(nums)
    while i<n:
        if nums[i]-1<n and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        else: i+=1
    for i in range(n):
        if nums[i]-1!=i: res.add(nums[i])
    return res

def find_corrupt_pair(nums:list[int])->list[int]:
    """
        We are given an unsorted array containing n numbers taken from the range 1 to n.
        The array originally contained all the numbers from 1 to n, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. 
        Find both these numbers.
        
        Output should return [<duplicate number>,<missing_number>]
    >>> find_corrupt_pair([3, 1, 2, 5, 2])
    [2, 4]
    >>> find_corrupt_pair([3, 1, 2, 3, 6, 4])
    [3, 5]
    """
    n = len(nums)
    i = 0
    while i<n:
        if nums[i]-1<n and nums[nums[i]-1]!=nums[i]:
            #be careful don't swap nums[i] first because it will effect other number
            nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        else: i+=1
    for i in range(n):
        if nums[i]-1!=i: return [nums[i],i+1]
    return []

if __name__=="__main__":
    import doctest
    doctest.testmod()