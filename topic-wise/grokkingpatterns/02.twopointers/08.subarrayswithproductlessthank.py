"""
Problem Statement
    Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

    Input: nums = [10,5,2,6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

    Input: nums = [1,2,3], k = 0
    Output: 0

Constraints:

    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106

Approach:
    This problem follows the Sliding Window and the Two Pointers pattern and shares similarities with Triplets with Smaller Sum with two differences:

    In this problem, the input array is not sorted.
    Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than the target. The implementation will be quite similar to Triplets with Smaller Sum.
"""

def sub_arrays_with_product_less_than_k(nums:list[int],k:int)->int:
    """Approach-1 
        Using Sliding Window
            1. Initialize two pointers, left and right both at 0, and initialize a variable product at 1.
            2. Expand the window to the right by incrementing right and multiplying product by nums[right].
            3. If product is now greater than or equal to k, contract the window from the left by dividing product by nums[left] and incrementing left. Do this until product is less than k again.
            4. After each step, add the size of the current window right - left + 1 to the result. This is because the new element at right could form that many new subarrays.
            5. Repeat steps 2-4 until right has traversed through the entire array.

    Intuition:
        since the product of all numbers from start to end is less than the target. 
        Therefore, all subarrays from start to end will have a product less than the target too; 
        to avoid duplicates, we will start with a subarray containing only arr[end] and then extend it

        why right - left + 1?
        Example [...5,6,3,4,8,...] right to number 5, left to number 8, (sub arrays ending at 8)
        All possible subarrays:
        [56348]
        [6348]
        [348]
        [48]
        [8]
        5 = right - left + 1

    Args:
        nums (list[int]): input list of integers
        k (int): target value k

    Returns:
        int: _description_
    """
    #as per given constraints nums[i]>=1
    if k<=1: return 0
    cnt = 0
    n = len(nums)
    product = 1
    window_start = 0
    for window_end in range(n):
        product*=nums[window_end]
        while product>=k and window_start<n:
            product /= nums[window_start]
            window_start+=1
        #This is because the new element at right could form that many new subarrays.(Gives sub arrays ending at window_end)
        cnt+=window_end-window_start+1
    return cnt

def get_all_sub_arrays_with_product_less_than_k(nums:list[int],k:int)->list[int]:
    """
        Time Complexity: O(N3)
            The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2) in the worst case. Therefore overall, our algorithm will take O(N^3).
        Space Complexity: O(N)
            Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
    """
    output = []
    product = 1
    n = len(nums)
    window_start = 0
    for window_end in range(n):
        product *=nums[window_end]
        while product>=k and window_start<n:
            product/=nums[window_start]
            window_start+=1
        #get sub_arrays from window size with numbers ending with window_end
        tmp_lst = []
        for i in range(window_end,window_start-1,-1):
            tmp_lst.insert(0,nums[i])
            output.append(tmp_lst.copy())
    return output

if __name__=="__main__":
    print(sub_arrays_with_product_less_than_k(nums = [10,5,2,6], k = 100))#8
    print(sub_arrays_with_product_less_than_k(nums = [1,2,3], k = 0))#0
    print(sub_arrays_with_product_less_than_k(nums=[57,44,92,28,66,60,37,33,52,38,29,76,8,75,22],k=18))#1

    #[[2], [5], [2, 5], [3], [5, 3], [10]]
    print(get_all_sub_arrays_with_product_less_than_k(nums = [2, 5, 3, 10], k = 30))
    