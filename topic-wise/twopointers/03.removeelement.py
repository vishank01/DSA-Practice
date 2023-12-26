"""
https://leetcode.com/problems/remove-element/submissions/1128848381/

Problem Statement:
    Given an unsorted array of numbers and a target key, remove all instances of key in-place and return the new length of the array.
"""
def remove_element(nums:list[int],key:int)->int:
    """
        Approach:
            Store required elements under slow pointer
    """
    slow_ptr = 0
    for fast_ptr in range(len(nums)):
        if nums[fast_ptr]!=key:
            nums[slow_ptr] = nums[fast_ptr]
            slow_ptr+=1
    return slow_ptr
        

if __name__ == "__main__":
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))#4
    print(remove_element([2, 11, 2, 2, 1], 2))#2
    print(remove_element([3,2,2,3], 3))#2