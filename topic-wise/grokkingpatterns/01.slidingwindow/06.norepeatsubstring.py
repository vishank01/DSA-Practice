"""
No-repeat Substring

Problem Statement

    Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating 
    characters is "abc".

Example 2:

    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating 
    characters is "ab".

Example 3:

    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating 
    characters are "abc" & "cde".

Solution

    This problem follows the Sliding Window pattern and we can use a similar dynamic sliding window strategy as discussed in Longest Substring with K Distinct Characters. 
    We can use a HashMap to remember the last index of each character we have processed. Whenever we get a repeating character we will shrink our sliding window to ensure that we always have distinct characters in the sliding window.
"""

def no_repeat_sub_string(s:str)->int:
    window_start=0
    maximum_window_size = 0
    window_data :dict[str,int] = {}
    for window_end in range(len(s)):
        window_data[s[window_end]] = window_data.get(s[window_end],0)+1
        while window_data.get(s[window_end])>1:
            window_data[s[window_start]]-=1
            if window_data[s[window_start]]==0:
                window_data.pop(s[window_start])
            window_start+=1
        maximum_window_size = max(maximum_window_size,window_end-window_start+1)
    return maximum_window_size

if __name__=="__main__":    
    print(no_repeat_sub_string("aabccbb"))
    print(no_repeat_sub_string("abbbb"))
    print(no_repeat_sub_string("abccde"))