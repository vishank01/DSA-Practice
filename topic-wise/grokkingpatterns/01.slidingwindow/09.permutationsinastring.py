"""
Problem:
    567. Permutation in String

    Given two strings s1 and s2, return true if s2 contains the permutation of s1.
    In other words, one of s1's permutations is the substring of s2.

Example 1:

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.

Solution:

    We have to find a substring in s2 such that the frequency of the characters in that substring is same as the frequency of the characters in s1
    So we will be using SLIDING WINDOW APPROACH to find such a window in s2 in which the freq of characters is same as s1. 

        1. The first step is to find the freq of all characters of s1.
        2. Then we will be starting with a window of size 1 initially in s2. That means start=0, end=0.
        3. Along with this, we will also be maintaining the frequency of the characters in the current window.
        4. We will be continuing the below steps untill we reach a situation where the end of the window reaches the end of s2. That means we will be doing the steps while end<length of s2.
                a) Increase the frequency of the character which is just now newly included inside the window. That means increase the frequency of s2[end].
                b) Now check if the frequency of the characters in the current window, is same as the frequency of characters int s1. But this is only possible if the length of current substring(window) is same as the length of s1. If this is true, then we can directly return true from here.
                c) If the frequency doesnt match, we have to change the window:-
                            i) If the length of window is less than the length of s1, then we should increase the length of the the window by increasing the end. So end+=1.
                            ii) If not, that means length of window is greater than or equal to the length of s1, so we will need to move to a new window. For that we will have to move start to the next character but before that we will have to decrease the frequency of start character from the curr window frequency. That means
                                    -Decrese the frequency of s2[start].
                                    -Move start to the next element.
                                    -Move end to the next element.
        5. If the algorithm did not return true for any window, then we will reach here(out of the loop). This will mean that we did not find any such substring in s2. So return false.
		  
"""

def permutations_in_a_string(s1:str,s2:str)->bool:
    window_start = 0
    freq_s1:dict[str,int] = {}
    freq_s2:dict[str,int] = {}
    for chr in s1:
        freq_s1[chr] = freq_s1.get(chr,0)+1
    for window_end in range(len(s2)):
        freq_s2[s2[window_end]] = freq_s2.get(s2[window_end],0)+1
        while window_end-window_start+1>len(s1):
            freq_s2[s2[window_start]]-=1
            if freq_s2[s2[window_start]]==0:
                freq_s2.pop(s2[window_start])
            window_start+=1
        if len(freq_s1)==len(freq_s2):
            match_cnt = 0
            for chr in freq_s1:
                if freq_s2.get(chr,0)!=freq_s1[chr]:
                    break
                match_cnt+=1
            if match_cnt==len(freq_s1):
                return True
    return False

if __name__=="__main__":
    print(permutations_in_a_string(s1 = "ab", s2 = "eidbaooo"))#True
    print(permutations_in_a_string(s1 = "ab", s2 = "eidboaoo"))#False
    print(permutations_in_a_string(s1 = "hello", s2 = "ooolleoooleh"))#False
    print(permutations_in_a_string(s1 = "abcdxabcde", s2 = "abcdeabcdx"))#True