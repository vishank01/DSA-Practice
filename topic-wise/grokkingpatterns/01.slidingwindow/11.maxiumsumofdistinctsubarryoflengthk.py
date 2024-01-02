"""
2461. Maximum Sum of Distinct Subarrays With Length K

Problem Statement:
    You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
        1. The length of the subarray is k, and
        2. All the elements of the subarray are distinct.
    Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
    A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:

    Input: nums = [1,5,4,2,9,9,9], k = 3
    Output: 15
    Explanation: The subarrays of nums with length 3 are:
    - [1,5,4] which meets the requirements and has a sum of 10.
    - [5,4,2] which meets the requirements and has a sum of 11.
    - [4,2,9] which meets the requirements and has a sum of 15.
    - [2,9,9] which does not meet the requirements because the element 9 is repeated.
    - [9,9,9] which does not meet the requirements because the element 9 is repeated.
    We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:

    Input: nums = [4,4,4], k = 3
    Output: 0
    Explanation: The subarrays of nums with length 3 are:
    - [4,4,4] which does not meet the requirements because the element 4 is repeated.
    We return 0 because no subarrays meet the conditions.

Constraints:

    1 <= k <= nums.length <= 105
    1 <= nums[i] <= 105
"""

def maximum_sum_of_distinct_sub_array_of_length_k(nums: list[int], k: int) -> int:
        window_sum = 0
        window_data = {}
        window_start = 0
        max_sum = float('-inf')
        for window_end in range(len(nums)):
            window_sum +=nums[window_end]
            window_data[nums[window_end]]= window_data.get(nums[window_end],0)+1
            while len(window_data)>k or window_data[nums[window_end]]>1:
                window_data[nums[window_start]]-=1
                if window_data[nums[window_start]]==0:
                    window_data.pop(nums[window_start])
                window_sum-=nums[window_start]
                window_start+=1
            if window_end-window_start+1==k:
                max_sum = max(max_sum,window_sum)
        return max_sum if max_sum!=float("-inf") else 0

if __name__=="__main__":
    print(maximum_sum_of_distinct_sub_array_of_length_k([1,5,4,2,9,9,9],3))