"""
Given text string with length n and a pattern with length m, the task is to prints all occurrences of pattern in text. 
Note: You may assume that n > m.

Examples: 

    Input:  text = “THIS IS A TEST TEXT”, pattern = “TEST”
    Output: Pattern found at index 10

    Input:  text =  “AABAACAADAABAABA”, pattern = “AABA”
    Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

The time complexity of the Rabin-Karp Algorithm is O(n+m) in the worst case. 
"""

def search_rabin_karp(string:str,pattern:str):
    """sliding window+hashes to compare pattern"""
    window_start = 0
    len_s = len(string)
    len_pattern = len(pattern)
    pattern_hash = hash(pattern)
    for window_end in range(len_s):
        if window_end-window_start+1>=len_pattern:
            if hash(string[window_start:window_end+1])==pattern_hash:
                print(f"Pattern {pattern} found at {window_start}")
            window_start+=1
if __name__=="__main__":
    search_rabin_karp("THIS IS A TEST TEXT","TEST")
    search_rabin_karp("AABAACAADAABAAABAA","AABA")