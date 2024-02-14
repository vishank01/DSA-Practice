"""
Given text string with length n and a pattern with length m, the task is to prints all occurrences of pattern in text. 
Note: You may assume that n > m.

Examples: 

    Input:  text = “THIS IS A TEST TEXT”, pattern = “TEST”
    Output: Pattern found at index 10

    Input:  text =  “AABAACAADAABAABA”, pattern = “AABA”
    Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

Naive Pattern Searching algorithm: 
    1. Slide the pattern over text one by one and check for a match. 
    2. If a match is found, then slide (j) by 1 again to check for subsequent matches.
    3. If mismatch occurs, break the loop and reset j to 0.

Time Complexity: 
    The worst case complexity of the Naive algorithm is O(mn)

Disadvantages:
    1. The Naive pattern-searching algorithm doesn't work well in cases where we see many matching characters followed by a mismatching character.
        Examples:
            1. txt[] = “AAAAAAAAAAAAAAAAAB”, pat[] = “AAAAB”
            2. txt[] = “ABABABCABABABCABABABC”, pat[] =  “ABABAC” (not a worst case, but a bad case for Naive)
"""

def search(string:str,pattern:str):
    len_s,len_p = len(string),len(pattern)
    for i in range(len_s):
        j=0
        while j<len_p:
            #check if character at s matches with character at j if not then restore j to 0
            if i+j<len_s and string[i+j]==pattern[j]:
                j+=1
            else:
                break
            if j==len_p:
                print(f"Pattern '{pattern}' found at index {i}")
    
if __name__=="__main__":
    search("THIS IS A TEST TEXT","TEST")
    search("AABAACAADAABAAABAA","AABA")