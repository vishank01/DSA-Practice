"""
Problem Statement
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

    Input: [2, 3, 4, 1, 5], k=2 
Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sum_sub_array(array:list[int],k:int)->int:
    max_sum = 0
    running_sum = 0
    for i in range(len(array)):
        if i<k:
            running_sum+=array[i]
        else:
            running_sum=running_sum-array[i-k]+array[i]
        if i>=k-1:
            max_sum = max(running_sum,max_sum)
    return max_sum

if __name__=="__main__":
    print(max_sum_sub_array([2, 1, 5, 1, 3, 2],3))
    print(max_sum_sub_array([2, 3, 4, 1, 5],2))