"""
Given text string with length n and a pattern with length m, the task is to prints all occurrences of pattern in text. 
Note: You may assume that n > m.

Examples: 

    Input:  text = “THIS IS A TEST TEXT”, pattern = “TEST”
    Output: Pattern found at index 10

    Input:  text =  “AABAACAADAABAABA”, pattern = “AABA”
    Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

The time complexity of the KMP algorithm is O(n+m) in the worst case. 


KMP (Knuth Morris Pratt) Pattern Searching:

    1. The Naive pattern-searching algorithm doesn't work well in cases where we see many matching characters followed by a mismatching character.
        Examples:
            1. txt[] = “AAAAAAAAAAAAAAAAAB”, pat[] = “AAAAB”
            2. txt[] = “ABABABCABABABCABABABC”, pat[] =  “ABABAC” (not a worst case, but a bad case for Naive)
    2. The KMP matching algorithm uses degenerating property (pattern having the same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst-case complexity to O(n+m). 
    3. he basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window.
    4. We take advantage of this information to avoid matching the characters that we know will anyway match. 


Matching Overview

        txt = “AAAAABAAABA” 
        pat = “AAAA”
        We compare first window of txt with pat

        txt = “AAAAABAAABA” 
        pat = “AAAA”  [Initial position]
        We find a match. This is same as Naive String Matching.

        In the next step, we compare next window of txt with pat.

        txt = “AAAAABAAABA” 
        pat =  “AAAA” [Pattern shifted one position]

    This is where KMP does optimization over Naive. In this second window, we only compare fourth A of pattern
    with fourth character of current window of text to decide whether current window matches or not.
    Since we know first three characters will anyway match, we skipped matching first three characters. 

Need of Preprocessing?

    An important question arises from the above explanation, how to know how many characters to be skipped.
    To know this, we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be skipped

Pre-Processing:
    lps indicates the longest proper prefix which is also a suffix.
    A proper prefix is a prefix with a whole string not allowed.
    For example
        Prefixes of “ABC” are “”, “A”, “AB” and “ABC”.
        Proper prefixes are “”, “A” and “AB”. Suffixes of the string are “”, “C”, “BC”, and “ABC”.

Examples of lps[] construction:

    For the pattern “AAAA”, lps[] is [0, 1, 2, 3]
    For the pattern “ABCDE”, lps[] is [0, 0, 0, 0, 0]
    For the pattern “AABAACAABAA”, lps[] is [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    For the pattern “AAACAAAAAC”, lps[] is [0, 1, 2, 0, 1, 2, 3, 3, 3, 4] 
    For the pattern “AAABAAA”, lps[] is [0, 1, 2, 0, 1, 2, 3]

Preprocessing Algorithm:

    In the preprocessing part, 

        1. We calculate values in lps[]. To do that, we keep track of the length of the longest prefix suffix value (we use len variable for this purpose) for the previous index
        2. We initialize lps[0] and len as 0.
        3. If pat[len] and pat[i] match, we increment len by 1 and assign the incremented value to lps[i].
        4. If pat[i] and pat[len] do not match and len is not 0, we update len to lps[len-1]

Illustration of preprocessing (or construction of lps[]):

    pat[] = “AAACAAAA”
    => len = 0, i = 0: 
    lps[0] is always 0, we move to i = 1
    => len = 0, i = 1:

    Since pat[len] and pat[i] match, do len++, 
    store it in lps[i] and do i++.
    Set len = 1, lps[1] = 1, i = 2
    => len = 1, i  = 2:

    Since pat[len] and pat[i] match, do len++, 
    store it in lps[i] and do i++.
    Set len = 2, lps[2] = 2, i = 3
    => len = 2, i = 3:

    Since pat[len] and pat[i] do not match, and len > 0, 
    Set len = lps[len-1] = lps[1] = 1
    => len = 1, i = 3:

    Since pat[len] and pat[i] do not match and len > 0, 
    len = lps[len-1] = lps[0] = 0
    => len = 0, i = 3:

    Since pat[len] and pat[i] do not match and len = 0, 
    Set lps[3] = 0 and i = 4
    => len = 0, i = 4:

    Since pat[len] and pat[i] match, do len++, 
    Store it in lps[i] and do i++. 
    Set len = 1, lps[4] = 1, i = 5
    => len = 1, i = 5:

    Since pat[len] and pat[i] match, do len++, 
    Store it in lps[i] and do i++.
    Set len = 2, lps[5] = 2, i = 6
    => len = 2, i = 6:

    Since pat[len] and pat[i] match, do len++, 
    Store it in lps[i] and do i++.
    len = 3, lps[6] = 3, i = 7
    => len = 3, i = 7:

    Since pat[len] and pat[i] do not match and len > 0,
    Set len = lps[len-1] = lps[2] = 2
    => len = 2, i = 7:

    Since pat[len] and pat[i] match, do len++, 
    Store it in lps[i] and do i++.
    len = 3, lps[7] = 3, i = 8
    We stop here as we have constructed the whole lps[].

Implementation of KMP algorithm:

    Unlike the Naive algorithm, where we slide the pattern by one and compare all characters at each shift, 
    we use a value from lps[] to decide the next characters to be matched. The idea is to not match a character that we know will anyway match.

Below is the illustration of the above algorithm:

    Consider txt[] = “AAAAABAAABA“, pat[] = “AAAA“

    If we follow the above LPS building process then lps[] = {0, 1, 2, 3} 

    -> i = 0, j = 0: txt[i] and pat[j] match, do i++, j++
    -> i = 1, j = 1: txt[i] and pat[j] match, do i++, j++
    -> i = 2, j = 2: txt[i] and pat[j] match, do i++, j++
    -> i = 3, j = 3: txt[i] and pat[j] match, do i++, j++
    -> i = 4, j = 4: Since j = M, print pattern found and reset j, j = lps[j-1] = lps[3] = 3

    Here unlike Naive algorithm, we do not match first three 
    characters of this window. Value of lps[j-1] (in above step) gave us index of next character to match.

    -> i = 4, j = 3: txt[i] and pat[j] match, do i++, j++
    -> i = 5, j = 4: Since j == M, print pattern found and reset j, j = lps[j-1] = lps[3] = 3
    Again unlike Naive algorithm, we do not match first three characters of this window. Value of lps[j-1] (in above step) gave us index of next character to match.

    -> i = 5, j = 3: txt[i] and pat[j] do NOT match and j > 0, change only j. j = lps[j-1] = lps[2] = 2
    -> i = 5, j = 2: txt[i] and pat[j] do NOT match and j > 0, change only j. j = lps[j-1] = lps[1] = 1
    -> i = 5, j = 1: txt[i] and pat[j] do NOT match and j > 0, change only j. j = lps[j-1] = lps[0] = 0
    -> i = 5, j = 0: txt[i] and pat[j] do NOT match and j is 0, we do i++. 
    -> i = 6, j = 0: txt[i] and pat[j] match, do i++ and j++
    -> i = 7, j = 1: txt[i] and pat[j] match, do i++ and j++

    We continue this way till there are sufficient characters in the text to be compared with the characters in the pattern…
"""