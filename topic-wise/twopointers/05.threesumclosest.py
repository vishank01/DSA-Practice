"""
https://leetcode.com/problems/3sum-closest/submissions/1129059994

Problem Statement: 

    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

Example 1:

    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

    Input: nums = [0,0,0], target = 1
    Output: 0
    Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
    
Constraints:

    3 <= nums.length <= 500
    -1000 <= nums[i] <= 1000
    -104 <= target <= 104

To meet the condition i != j != k we need to make sure that each number is not used more than once.
"""

def three_sum_closest(nums:list[int],target:int)->int:
    """
        a+b+c-target is min = x (let's say). Now find x
    """
    nums.sort()
    n = len(nums)
    min_triplet_sum = 0
    closest_sum = float('inf')
    for i in range(n-2):
        start,end = i+1,n-1
        while start<end:
            s = nums[i]+nums[start]+nums[end]
            if s<target:
                start+=1
            elif s>target:
                end-=1
            else: start+=1;end-=1
            if abs(s-target)<closest_sum:
                min_triplet_sum = s
                closest_sum = abs(s-target)
    return min_triplet_sum

if __name__=="__main__":
    print(three_sum_closest(nums = [-1,2,1,-4], target = 1))#2
    # print(three_sum_closest(nums = [0,0,0], target = 1))#0
    # print(three_sum_closest(nums = [1,1,1,0],target=-100))#2
