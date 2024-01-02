"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1128837740

Problem Statement:
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Intuition:
    1. Use a slow pointer to "lock" the "wanted" element, and use a fast pointer to move forward along the list and look for new unique elements in the list.
    2. Or, in other words, the current slow pointer is used to locate the latest unique number for the results, and fast is used for iterating and discovery.

Solution:    
    In this problem, we need to remove the duplicates In-place such that the resultant length of the array remains sorted. 
     
        1. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we encounter duplicates. 
        2. In other words, we will keep one pointer for iterating the array and one pointer for placing the next non-duplicate number.
        3. So our algorithm will be to iterate the array and whenever we see a non-duplicate number we move it next to the last non-duplicate number we’ve seen.
"""

def remove_duplicates(nums:list[int])->list[int]:
    slow_ptr=0
    for fast_ptr in range(1,len(nums)):
        #update slow pointer slow_ptr when unique element is seen
        if nums[fast_ptr]!=nums[slow_ptr]:
            slow_ptr+=1
            nums[slow_ptr]=nums[fast_ptr]
    #elements till slow_ptr will be unique, slow_ptr+1 is used in slicing to include j
    return nums[:slow_ptr+1]
        
if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))