def character_transform(n:int)->str:
    """generate string by combining two alphabets to the next coming alphabet until we reach Z 
        e.g, n=5 means AAAAA -> BBA -> CA
    Args:
        n (int): number of A's present in a string

    Returns:
        str: returns transformed character string

    >>> character_transform(67108876)
    'ZZDC'
    >>> character_transform(19)
    'EBA'
    >>> character_transform(11)
    'DBA'
    >>> character_transform(8)
    'D'
    """
    op = []
    chr_val = 65
    while(n>0):
        if chr_val<90:
            #check if number is odd and store last character value in output
            if n%2!=0:
                op.append(chr(chr_val))
            #increment char value (e.g, from A to B while doing right shift)
            chr_val+=1
        else:
            op.append(chr(chr_val))
        #right shift divides data by 2
        n=n>>1
    return "".join(op[::-1])

def char_transform_recursion(n:int,prev_char:int=65):
    """generate string by combining two alphabets to the next coming alphabet until we reach Z 
        e.g, n=5 means AAAAA -> BBA -> CA
    Args:
        n (int): number of A's present in a string

    Returns:
        str: returns transformed character string

    >>> character_transform(67108876)
    'ZZDC'
    >>> character_transform(19)
    'EBA'
    >>> character_transform(11)
    'DBA'
    >>> character_transform(8)
    'D'
    """
    if prev_char==90: return "Z"*n
    if n<=0: return ""
    if n%2==0:
        ans = char_transform_recursion(n>>1,prev_char+1)
    else:
        ans = char_transform_recursion(n>>1,prev_char+1)+chr(prev_char)
    return ans

if __name__=="__main__":
    import doctest
    doctest.testmod()
    print(char_transform_recursion(67108876))