def character_transform(n:int)->str:
    """generate string by combining two alphabets to the next coming alphabet until we reach Z 
        e.g, n=5 means AAAAA -> BBA -> CA
    Args:
        n (int): number of A's present in a string

    Returns:
        str: [description]

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

if __name__=="__main__":
    import doctest
    doctest.testmod()