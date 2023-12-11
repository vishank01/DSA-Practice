#recursive
def longest_common_subsequence(s1:str,s2:str)->str:
    """Recursive implementation of lcs on given strings s1 and s2
        Disadvantages:
            solves already solved problems (can be avoid using memoization)
            recursive solution may ray out of resources due to time complexity involved
            stack overflow occurs if more than recursive limit calls are made
    Args:
        s1 (str): string1
        s2 (str): string2

    Returns:
        str: returns lcs of s1 and s2
    
    >>> longest_common_subsequence('vishnu','shashank')
    'shn'
    """
    def lcs_helper(s1:str,s2:str,m:int,n:int)->str:
        """Base case:
            If length of s1 or s2 is 0 return empty string
           Induction:
            check if last character of s1 and s2 matches if so decrement m and n
            otherwise in one branch do m-1,in another do n-1 and finally take string with max length among branches

        Args:
            s1 (str): string1
            s2 (str): string2
            m (int): length of string1
            n (int): length of string2

        Returns:
            str: lcs of s1 and s2
        """
        if m==0 or n==0:
            return ""
        else:
            if s1[m-1]==s2[n-1]:
                return lcs_helper(s1,s2,m-1,n-1)+s1[m-1]
            else:
                x = lcs_helper(s1,s2,m-1,n)
                y = lcs_helper(s1,s2,m,n-1)
                return x if len(x)>len(y) else y
    return lcs_helper(s1,s2,len(s1),len(s2))
        
#recursive+memoization
def longest_common_subsequence_memoized(s1:str,s2:str)->str:
    cache: list = []
    """Recursive+Memoization implementation of lcs on given strings s1 and s2
        Disadvantages:
            recursive solution may ray out of resources due to time complexity involved
            stack overflow occurs if more than recursive limit calls are made
    Args:
        s1 (str): string1
        s2 (str): string2

    Returns:
        str: returns lcs of s1 and s2
    
    >>> longest_common_subsequence_memoized('vishnu','shashank')
    'shn'
    """

    def lcs_helper(s1:str,s2:str,m:int,n:int)->str:
        if cache[m][n]!="":
            return cache[m][n]
        if m==0 or n==0:
            cache[m][n] = ""
        else:
            if s1[m-1]==s2[n-1]:
                cache[m][n] = lcs_helper(s1,s2,m-1,n-1)+s1[m-1]
            else:
                _str1 = lcs_helper(s1,s2,m-1,n)
                _str2 = lcs_helper(s1,s2,m,n-1)
                cache[m][n] = _str1 if len(_str1)>len(_str2) else _str2
        return cache[m][n]

    m,n = len(s1),len(s2)
    #initialize array with size m+1 and n+1
    cache = [["" for _ in range(n+1)] for _ in range(m+1)]
    return lcs_helper(s1,s2,m,n)

#topdown approach
def longest_common_subsequence_topdown(s1:str,s2:str)->str:
    """Topdown implementation of lcs on given strings s1 and s2
        more reference on youtube video https://www.youtube.com/watch?v=g_hIx4yn9zg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=21
    Args:
        s1 (str): string1
        s2 (str): string2

    Returns:
        str: returns lcs of s1 and s2
    
    >>> longest_common_subsequence_topdown('vishnu','shashank')
    'shn'
    """
    cache = [["" for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                cache[i][j] = cache[i-1][j-1]+s1[i-1]
            else:
                cache[i][j] = cache[i-1][j] if len(cache[i-1][j])>len(cache[i][j-1]) else cache[i][j-1]
    return cache[len(s1)][len(s2)]


if __name__=="__main__":
    import doctest
    doctest.testmod()