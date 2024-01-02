"""
Longest Substring with Same Letters after Replacement 

Problem:

    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    Intution:

The question asks to find the longest substring that contains the same characters. It also says that we can change k characters to make a substring longer and valid.

Ex:

    "ABAB" k = 1
    Here we know that we can change 1 character to make a substring that is a valid answer
    AKA: a substring with all the same characters.

    So a valid substring answer would be s.substring(0, 3) -> "ABA" because with can replace 1 character.

    Another answer could be "BAB".

    Using the sliding window technique, we set up pointers left = 0 and right = 0
    We know that a our current window / substring is valid when the number of characters that need to be replaced is <= k.

    Lets take the example below to understand it better:
Ex:

    "AABABCC" k = 2
    left = 0
    right = 4 inclusive
    This is example above shows a valid substring window because we have enough k changes to change the B's to A's and match the rest of the string.

    "AABAB" with 2 changes is valid

    We will need to know how many letters in our substring that we need to replace.
    To find out the lettersToReplace = (end - start + 1) - mostFreqLetter;
    Pretty much you take the size of the window minus the most freq letter that is in the current window.

    Now that we know how many characters that need to be replaced in our window, we can deduce that if lettersToReplace > k than the window is invalid and we decrease the window size from the left.

    Pulling the whole algorithm together we get:

"""

def longest_sub_string_with_same_letters(s:str,k:int)->int:
    window_start = 0
    max_window_size = 0
    most_freq_letter_cnt = 0
    window_data:dict[str,int] = {}
    for window_end in range(len(s)):
        window_data[s[window_end]] = window_data.get(s[window_end],0)+1
        most_freq_letter_cnt = max(most_freq_letter_cnt,window_data[s[window_end]])
        letters_to_change = window_end-window_start+1-most_freq_letter_cnt
        if letters_to_change>k:
            window_data[s[window_start]]-=1
            if window_data[s[window_start]]==0:
                window_data.pop(s[window_start])
            window_start+=1
        max_window_size = max(max_window_size,window_end-window_start+1)
    return max_window_size

if __name__=="__main__":
    print(longest_sub_string_with_same_letters("ABAB",2))
    print(longest_sub_string_with_same_letters("AABABCC",2))
    print(longest_sub_string_with_same_letters("AABABBA",1))