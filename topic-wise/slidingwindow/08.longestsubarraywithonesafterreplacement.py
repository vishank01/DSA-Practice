"""
Problem:

    Max Consecutive Ones III
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

def longest_sub_array_with_ones_after_replacement(array:list[int],k:int)->int:
    window_start = 0
    max_window_size = 0
    window_data :dict[str,int] = {}
    for window_end in range(len(array)):
        window_data[array[window_end]] = window_data.get(array[window_end],0)+1
        #put a check on number of zeros to be inside window, if it crosses k then remove elements from start
        while window_data.get(0,0)>k:
            window_data[array[window_start]]-=1
            if window_data[array[window_start]]==0:
                window_data.pop(array[window_start])
            window_start+=1
        max_window_size = max(max_window_size,window_end-window_start+1)
    return max_window_size

def longest_sub_array_with_ones_after_replacement(array:list[int],k:int)->int:
    zero_count = 0
    #slow pointer
    window_start = 0
    max_window_size = 0
    for window_end in range(len(array)):
        if array[window_end]==0:
            zero_count+=1
        #put a check on number of zeros to be inside window, if it crosses k then remove elements from start
        while zero_count>k:
            if array[window_start]==0:
                zero_count-=1
            window_start+=1
        max_window_size = max(max_window_size,window_end-window_start+1)
    return max_window_size

if __name__=="__main__":
    print(longest_sub_array_with_ones_after_replacement([1,1,1,0,0,0,1,1,1,1,0],2))
    print(longest_sub_array_with_ones_after_replacement([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))