def find_permutations_recursion(input_array:str)->list[str]:
    """This is generating permutations recursion without using backtracking
        this approach uses pass by value (new inputs and outputs are created in every call)
        more details https://youtu.be/zC4D7cuaYzo?list=PL_z_8CaSLPWdbOTog8Jxk9XOjzUs3egMP&t=1969

        input output approach is used to make choice at every character and choosen character is added to op
        and reduced from ip. These choices are choosen from for loop

        Disadvantages:
            In this approach,new Input string is created in every recursive call and in case of larger inputs
            creating too many wiil consume more memory
    Args:
        input_array (str): input string for which permutations to be done
    Returns:
        list[str]: returns output
    >>> find_permutations_recursion("abc")
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> find_permutations_recursion("aab")
    ['aab', 'aba', 'baa']
    """
    def find_permutations_helper(ip:str,output:list[str],op:str="")->None:
        """
        helper function to perform permutations using recursion
        Args:
            ip (str): input string for which permutations to be done
            output (list[str] | None, optional): output that is used in internal recursive calls. Defaults to None.
            op (str, optional): used internally in recursive calls to store intermediate. Defaults to "".
        Returns (None)
        """
        maps = set()
        if len(ip)==0:
            #if input is 0 store output in output array
            output+=[op]
        else:
            for i in range(len(ip)):
                #this is controlled recursion where maps is used to avoid duplicate characters from inputs
                if ip[i] not in maps:
                    maps.add(ip[i])
                    #omit included character and add it to op
                    new_ip = ip[:i]+ip[i+1:]
                    new_op=op+ip[i]
                    find_permutations_helper(new_ip,output,new_op)
    output = []
    find_permutations_helper(input_array,output)
    return output

def find_permutations_backtracking(input_array:str)->list[str]:
    """This is generating permutations recursion using backtracking which uses pass by reference
    Args:
        input_array (str): input string for which permutations to be done
    Returns:
        list[str]: returns output
    >>> find_permutations_backtracking("abc")
    ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    >>> find_permutations_backtracking("aab")
    ['aab', 'aba', 'baa']
    """
    def find_permutations_helper(ip:list,left:int,right:int,output:list[str])->None:
        """
        helper function to perform permutations using recursion
        when left==right it means entire input list is traversed so one combination will be generated
        Args:
            ip (list): input list of characters for which permutations to be done
            left (int): left pointer for array
            right (int): right pointer for array
            output (list[str] | None, optional): output that is used in internal recursive calls. Defaults to None.
        Returns (None)
        """
        maps = set()
        if left==right:
            #left and right are equal then input array consists of one combination
            output+=["".join(ip)]
        else:
            for i in range(left,right+1):
                #this is controlled recursion where maps is used to avoid duplicate characters from inputs
                if ip[i] not in maps:
                    maps.add(ip[i])
                    ip[left],ip[i]=ip[i],ip[left]
                    find_permutations_helper(ip,left+1,right,output)
                    #backtrack operation
                    ip[left],ip[i]=ip[i],ip[left]
    output = []
    find_permutations_helper(list(input_array),0,len(input_array)-1,output)
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()