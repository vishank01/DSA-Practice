"""
https://leetcode.com/problems/backspace-string-compare/submissions/1131516755
https://leetcode.com/problems/backspace-string-compare/submissions/1131494535

Problem Statement:
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.

Example 1:

    Input: s = "ab#c", t = "ad#c"
    Output: true
    Explanation: Both s and t become "ac".

Example 2:

    Input: s = "ab##", t = "c#d#"
    Output: true
    Explanation: Both s and t become "".

Example 3:

    Input: s = "a#c", t = "b"
    Output: false
    Explanation: s becomes "c" while t becomes "b".

Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?

"""

def compare_using_stack(s:str,t:str)->bool:

    def get_string(s:str)->list:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i]=="#":
                if stack:
                    stack.pop(-1)
            else:
                stack.append(s[i])
        return stack
    
    return get_string(s)==get_string(t)
        
def compare_using_two_pointers(s:str,t:str)->bool:
    """
        Approach:
            To compare the given strings, first, we need to apply the backspaces. 
                1. An efficient way to do this would be from the end of both the strings. 
                2. We can have separate pointers, pointing to the last element of the given strings. 
                3. We can start comparing the characters pointed out by both the pointers to see if the strings are equal. 
                4. If, at any stage, the character pointed out by any of the pointers is a backspace (#), 
                5. we will skip and apply the backspace until we have a valid character available for comparison.
    """
    m,n = len(s),len(t)
    i,j = m-1,n-1

    def get_next_char_idx(string:str,index)->int:
        backspaces_cnt = 0
        while index>=0:
            if string[index]=="#":
                backspaces_cnt+=1
            elif backspaces_cnt>0:
                backspaces_cnt-=1
            else:
                break
            #skip a backspace or valid character because backspaces_cnt>0
            index-=1
        return index

    while i>=0 or j>=0:
        i = get_next_char_idx(s,i)
        j = get_next_char_idx(t,j)
        if i<0 and j<0:
            #both have reached end of strings
            return True
        elif i<0 or j<0:
            return False
        if s[i]!=t[j]:
            return False
        i-=1;j-=1
    return True

if __name__=="__main__":
    print(compare_using_two_pointers(s = "ab#c", t = "ad#c"))#true
    print(compare_using_two_pointers(s = "y#fo##f",t = "y#f#o##f"))#true