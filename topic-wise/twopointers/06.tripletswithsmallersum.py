"""
Problem Statement:

Given an array arr[] of distinct integers of size N and a value sum, the task is to find the count of triplets (i, j, k),
having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.


Example 1:

    Input: N = 4, sum = 2
    arr[] = {-2, 0, 1, 3}
    Output:  2
    Explanation: Below are triplets with 
    sum less than 2 (-2, 0, 1) and (-2, 0, 3). 
 

Example 2:


    Input: N = 5, sum = 12
    arr[] = {5, 1, 3, 4, 7}
    Output: 4
    Explanation: Below are triplets with 
    sum less than 12 (1, 3, 4), (1, 3, 5), 
    (1, 3, 7) and (1, 4, 5).


Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(1).

Constraints:
3 ≤ N ≤ 103
-103 ≤ arr[i] ≤ 103

To meet the condition i != j != k we need to make sure that each number is not used more than once.
"""

def triplets_with_smaller_sum(nums:list[int],target:int)->int:
    nums.sort()
    n = len(nums)
    cnt_of_triplets = 0
    for i in range(n-2):
        start,end = i+1,n-1
        while start<end:
            s = nums[i]+nums[start]+nums[end]
            if s<target:
                #since arr[end] >= arr[start], therefore, we can replace arr[end]
                #by any number between start and end to get a sum less than the targetSum
                cnt_of_triplets+=end-start
                start+=1
            elif s>=target:
                end-=1
    return cnt_of_triplets

if __name__ == "__main__":
    # print(triplets_with_smaller_sum([-2, 0, 1, 3],2))#2
    # print(triplets_with_smaller_sum([5, 1, 3, 4, 7],12))#4
    print(triplets_with_smaller_sum([30,8,23,6,10,9,31,7,19,20,1,33,21,27,28,3,25,26],86))