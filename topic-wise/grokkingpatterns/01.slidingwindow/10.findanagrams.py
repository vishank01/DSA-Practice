"""
String Anagrams

Problem:

    **** 438**.** Find All Anagrams in a String
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]

Explanation:

The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

    Input: s = "abab", p = "ab"
    Output: [0,1,2]

Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.
"""

def find_anagrams(s:str,p:str):
    output = []
    window_start = 0
    freq_s1:dict[str,int] = {};freq_s2:dict[str,int] = {}
    for chr in p: freq_s1[chr] = freq_s1.get(chr,0)+1
    for window_end in range(len(s)):
        freq_s2[s[window_end]] = freq_s2.get(s[window_end],0)+1
        while window_end-window_start+1>len(p):
            freq_s2[s[window_start]]-=1
            if freq_s2[s[window_start]]==0:
                freq_s2.pop(s[window_start])
            window_start+=1
        match_cnt = 0
        for chr in freq_s1:
            if freq_s1[chr]==freq_s2.get(chr,0):
                match_cnt+=1
        if match_cnt==len(freq_s1):
            output.append(window_start)
    return output

if __name__=="__main__":
    print(find_anagrams(s = "cbaebabacd", p = "abc"))#[0,6]
    print(find_anagrams(s = "abab", p = "ab"))#[0,1,2]