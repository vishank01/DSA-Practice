"""
Longest Substring with K Distinct Characters

Problem Statement
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more 
    than '2' distinct characters is "araa".

Example 2:

    Input: String="araaci", K=1
    Output: 2
    Explanation: The longest substring with no more 
    than '1' distinct characters is "aa".

Example 3:

    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more 
    than '3' distinct characters are "cbbeb" & "bbebi".

Solution:
    This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as discussed in Smallest Subarray with a given sum. 
    We can use a HashMap to remember the frequency of each character we have processed. Here is how we will solve this problem:

    1. First, we will insert characters from the beginning of the string until we have ‘K’ distinct characters in the HashMap.
    2. These characters will constitute our sliding window. We are asked to find the longest such window having no more than ‘K’ distinct characters. We will remember the length of this window as the longest window so far.
    3. After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise fashion.
    4. In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap is larger than ‘K.’ We will shrink the window until we have no more than ‘K’ distinct characters in the HashMap. This is needed as we intend to find the longest window.
    5. While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if its frequency becomes zero.
    6. At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its length.
"""

def longest_sub_string_with_k_distinct_chars(string:list[int],k:int):
    window_start = 0
    longest_window_size = 0
    hashmap:dict[str,int] = {}
    for window_end in range(len(string)):
        hashmap[string[window_end]]=hashmap.get(string[window_end],0)+1
        while len(hashmap)>k:
            hashmap[string[window_start]]-=1
            if hashmap[string[window_start]]==0:
                hashmap.pop(string[window_start])
            window_start+=1
        longest_window_size = max(longest_window_size,window_end-window_start+1)
        
    return longest_window_size

if __name__=="__main__":
    print(longest_sub_string_with_k_distinct_chars("araaci",2))
    print(longest_sub_string_with_k_distinct_chars("araaci",1))
    print(longest_sub_string_with_k_distinct_chars("cbbebi",3))