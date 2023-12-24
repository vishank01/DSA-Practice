"""
Problem Statement
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

Example 3:

    Input: nums = [5,4,-1,7,8]
    Output: 23

Explanation: 

    The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
"""

def max_sum_kadanes_algorithm(nums:list[int])->int:
    """
        Time Complexity : O(N), for iterating over nums once
        Space Complexity : O(1), only constant extra space is being used.
    """
    local_sum,global_sum = 0,float('-inf')
    for ele in nums:
        local_sum = max(ele,local_sum+ele)
        global_sum = max(global_sum,local_sum)
    return global_sum

def max_sum_recursion(nums:list[int])->int:
    """
        Time Complexity : O(N2) we are basically considering every subarray sum and choosing maximum of it.
        Space Complexity : O(N) for recursive space
    """
    def solve(i,must_pick):
        if i >= len(nums): return 0 if must_pick else float('-inf')
        return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
    return solve(0, False)

if __name__=="__main__":
    print(max_sum_recursion([-2,1,-3,4,-1,2,1,-5,4]))#6
    print(max_sum_recursion([5,4,-1,7,8]))#23