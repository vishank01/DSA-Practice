"""
Problem Statement:
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
    The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

Example 2:

    Input: nums = [2,0,1]
    Output: [0,1,2]
 
Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
    
Approach:
    Brute-Force:
        1. The brute force solution will be to use an in-place sorting algorithm like Heapsort which will take O(N*logN). 
        2. Can we do better than this? Is it possible to sort the array in one iteration?
    Two-Pointer:
        1. We can use a Two Pointers approach while iterating through the array. 
        2. Let’s say the two pointers are called low and high which are pointing to the first and the last element of the array respectively. 
        3. So while iterating, we will move all 0s before low and all 2s after high so that in the end, all 1s will be between low and high.
"""

def sort_colors(nums:list[int])->list[int]:
    n = len(nums)
    i=0
    low,high = 0,n-1
    #if i cross high, then all numbers are two and it will swap those to between low and high
    while i<=high:
        if nums[i]==0:
            nums[i],nums[low]=nums[low],nums[i]
            low+=1
            i+=1
        elif nums[i]==2:
            nums[i],nums[high]=nums[high],nums[i]
            #decrement high only, after the swap the number(worst case 0 gets swapped with i and high)
            #so if i is incremented, 0 will be in the middle of low and high so i should not be incremented
            high-=1
            i+=1
        else:
            i+=1
    return nums

if __name__=="__main__":
    print(sort_colors([2,0,2,1,1,0]))
    print(sort_colors([2,0,1]))