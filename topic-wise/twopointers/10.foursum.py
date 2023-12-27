"""
Problem Statement: Four Sum

    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

Example 1:

    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]

Constraints:

    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109
"""

def four_sum(nums:list[int],target:int)->list[list[int]]:
    """
        suppose numbers are a+b+c+d = target

        we check whether two consecutive elements are equal or not because if they are, we don't want them (solutions need to be unique) 
        and will skip to the next set of numbers. Also, there is an additional constrain in this line that i > 0. 
        This is added to take care of cases like nums = [1,1,1] and target = 3. If we didn't have i > 0, 
        then we'd skip the only correct solution and would return [] as our answer which is wrong (correct answer is [[1,1,1]]
    """
    nums.sort()
    output = []
    n = len(nums)
    for i in range(n-3):
        #this avoids giving duplicate data for [1,1,1,1] and target 4 as [[1,1,1,1],[1,1,1,1],[1,1,1,1]] instead of just [[1,1,1,1]]
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            search_pairs(nums,i,j,n,target,output)
    return output

def search_pairs(nums:list[int],first:int,second:int,n:int,target:int,output:list[int]):
    i,j = second+1,n-1
    #i and j cannot be equal as numbers should be distinct
    while i<j:
        s = nums[first]+nums[second]+nums[i]+nums[j]
        if s<target:
            i+=1
        elif s>target:
            j-=1
        else:
            output.append([nums[first],nums[second],nums[i],nums[j]])
            i+=1;j-=1
            while i<j and nums[i]==nums[i-1]:
                i+=1
            # while i<j and nums[j]==nums[j-1]:
            #     j-=1

def four_sum_recursive(nums:list[int],target:int)->list[list[int]]:
    """
        The approach used in this code is a recursive approach called N-sum. It works on a sorted list by breaking down the problem of finding a four sum into smaller subproblems of finding N-1 sum until it's broken down to N=2 which can be solved by using the 2 pointer approach.
        
        . To solve the problem of finding combinations of four numbers from a given list that add up to a target sum, you can follow these steps:
            1. Sort the given list of numbers in ascending order. This step helps in skipping duplicate elements later on.
            2. Define a recursive function called Nsum that takes the following parameters:

                The list of numbers.
                The target sum.
                The value of N (which is 4 in this case).
                The current result list.
                The final list of N-sums.
                Inside the Nsum function, handle the following edge cases:

        . If the length of the input list is less than N, or N is less than 2, or the target is less than the smallest possible sum or greater than the largest possible sum, return. 
            This ensures that the function stops when it's not possible to find a valid combination.
        
        . If N is 2, we reach the base case:

            1. Set two pointers, j and k, at the beginning and end of the list respectively.
            2. Iterate while j is less than k.
            3. Calculate the sum s of the current numbers at indices j and k.
            4. Adjust the pointers j and k based on the comparison of s with the target sum.
            5. Handle duplicate elements by incrementing j if the current element is the same as the previous element at index j, and decrementing k if the current element is the same as the previous element at index k.
        
        . If N is greater than 2:

            1. Use a loop with index i from 0 to len(nums)-N+1.
            2. Inside the loop, make a recursive call to Nsum with adjusted parameters, including the sublist starting from i+1, the target minus the current element, N-1, the current result appended with the current element, and the final N-sums list.
            3. Skip duplicate cases by checking if i is 0 or the current element is different from the previous element at index i-1.
            4. Sort the input list of numbers in ascending order. This step ensures that duplicate combinations are grouped together.

        . Initialize an empty list called foursums.

        . Call the Nsum function with the sorted numbers, target sum, 4 (for 4 numbers), an empty result list, and the foursums list.

        . Return the foursums list, which contains all the combinations of four numbers that add up to the target sum.

        By following these steps, you can effectively find the desired combinations of numbers. Let me know if you have any further questions!2


        Time complexity: O(N3)O(N^3)O(N3)
        Space complexity: O(N)O(N)O(N), where N is the length of the input list.
    """
    def Nsum(nums: list[int], target: int, N: int, result: list[int], Nsums: list[list[int]]):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
            return
        elif N == 2:
            j, k = 0, len(nums) - 1
            while j < k:
                s = nums[k] + nums[j]
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    Nsums.append(result + [nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j-1] == nums[j]:
                        j += 1
                    while k>j and nums[k+1] == nums[k]:
                        k -= 1
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    Nsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], Nsums)
    
    nums.sort()
    foursums = []
    Nsum(nums, target, 4, [], foursums)
    return foursums

if __name__=="__main__":
    #[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(four_sum(nums = [1,0,-1,0,-2,2], target = 0))
    print(four_sum_recursive(nums = [1,0,-1,0,-2,2], target = 0))
    print(four_sum(nums=[-1,0,-5,-2,-2,-4,0,1,-2],target=-9))
    print(four_sum_recursive(nums=[-1,0,-5,-2,-2,-4,0,1,-2],target=-9))

    print(four_sum(nums=[-3,-2,-1,0,0,1,2,3],target=0))
    print(four_sum_recursive(nums=[-3,-2,-1,0,0,1,2,3],target=0))