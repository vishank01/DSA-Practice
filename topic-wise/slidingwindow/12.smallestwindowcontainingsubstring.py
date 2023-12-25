"""
Smallest Window containing Substring (hard)

Problem Statement:
    78. Minimum Window Substring
        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
        The testcases will be generated such that the answer is unique.
        A substring is a contiguous sequence of characters within the string.

Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

Solution:
    This problem follows the Sliding Window pattern and has a lot of similarities with Permutation in a String with one difference. 
    In this problem, we need to find a substring having all characters of the pattern which means that the required substring can have some additional characters and doesnt need to be a permutation of the pattern. 
    Here is how we will manage these differences:
        1. We will keep a running count of every matching instance of a character.
        2. Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track of the smallest substring that has all the matching characters.
        3. We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to note here is that we could have redundant matching characters, e.g., we might have two a in the sliding window when we only need one a. In that case, when we encounter the first a, we will simply shrink the window without decrementing the matched count. We will decrement the matched count when the second a goes out of the window.
"""

def smallest_window_containing_sub_string(s:str,t:str)->str:
    freq_t:dict[str,int] = {}
    freq_s:dict[str,int] = {}
    min_window_size = float('inf')
    window_start = matched_cnt = 0
    window_result_start = window_result_end = None
    len_s,len_t,window_start,matched_cnt = len(s),len(t),0,0
    for ch in t: freq_t[ch] = freq_t.get(ch,0)+1
    for window_end in range(len_s):
        if freq_s.get(s[window_end],0)<freq_t.get(s[window_end],0):
            matched_cnt+=1
        freq_s[s[window_end]] = freq_s.get(s[window_end],0)+1
        #once t matches in s, try to shrink window and still see if minimum window can be achieved
        while matched_cnt == len_t:
            freq_s[s[window_start]] = freq_s.get(s[window_start],1)-1
            if freq_t.get(s[window_start],0)>freq_s[s[window_start]]:
                matched_cnt -=1
            if window_end-window_start+1<min_window_size:
                min_window_size = window_end-window_start+1
                window_result_start,window_result_end = window_start,window_end
            window_start+=1
    if window_result_start is not None and window_result_end is not None and window_result_start<=window_result_end:
        return s[window_result_start:window_result_end+1]
    return ""

if __name__=="__main__":
    print(smallest_window_containing_sub_string(s = "ADOBECODEBANC", t = "ABC"))#BANC
    print(smallest_window_containing_sub_string(s = "a", t = "a"))#a
    print(smallest_window_containing_sub_string(s = "a", t = "aa"))#''
    print(smallest_window_containing_sub_string(s= "bba", t = "ab"))#ba