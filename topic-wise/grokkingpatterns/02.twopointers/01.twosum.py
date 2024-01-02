"""
https://leetcode.com/problems/two-sum/submissions/1128818159/

Problem Statement:
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Brute-Force:
    1. Taking one number at a time and searching for the second number through Binary Search.
    2. The time complexity of this algorithm will be O(N*logN). Can we do better than this?
    
We can follow the Two Pointers approach, Given Sorted Array

    1. We will start with one pointer pointing to the beginning of the array and another pointing at the end. 
    2. At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do, we have found our pair; otherwise, we will do one of two things:
    3. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.
    4. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.
"""
def two_sum_brute_force(nums:list[int],target:int)->list[int]:
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []
            
def two_sum_two_pointers(nums:list[int],target:int)->list[int]:
    """
        As Array is Sorted and index are asked, we can use Two pointers approach, Otherwise Hashing to be used.
    """
    i,j = 0,len(nums)-1
    while i<=j:
        if nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            return [i,j]
    return []
        
def two_sum_hashing(nums:list[int],target:int)->list[int]:
    """
        This Approach works even if array is not sorted, e.g, https://leetcode.com/problems/two-sum/
    """
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return [d[nums[i]],i]
        d[target-nums[i]] = i
    return []

if __name__ == "__main__":
    print(two_sum_hashing([1, 2, 3, 4, 6], 6))#[1,3]
    print(two_sum_hashing([2, 5, 9, 11], 11))#[0,2]