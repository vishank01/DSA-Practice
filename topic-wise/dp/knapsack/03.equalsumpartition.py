"""// https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
The partition problem is to determine whether a given set can be partitioned into two subsets such that 
the sum of elements in both subsets is the same. 

"""
def equal_sum_partition_top_down(array:list[int])->bool:
    """The partition problem is to determine whether a given set can be partitioned into two subsets such that 
        the sum of elements in both subsets is the same. 

        >   S1+S2 = S 
        >   2S1 = S (as S1=S2)
        >   S1 = S/2 ()
        >   now look for subset sum with target S/2

    Args:
        array (list[int]): input array of integers

    Returns:
        bool: returns True/False

    >>> equal_sum_partition_top_down([1,5,11,15])
    True
    >>> equal_sum_partition_top_down([1,5,3])
    False
    """
    def helper(array:list[int],target:int,n:int)->bool:
        #be careful about base condition here, as 0 elements array with positive target is False
        if n==0:
            return True if target==0 else False
        else:
            if array[n-1]<=target:
                return helper(array,target-array[n-1],n-1) or helper(array,target,n-1)
            else:
                return helper(array,target,n-1)
    
    array_sum = sum(array)
    if array_sum%2!=0: 
        return False
    else:
        target = array_sum//2
    return helper(array,target,len(array))

def subset_sum_bottom_up(array:list[int])->bool:
    """Given set of non-negative integers and target value, function returns True/False based on
    whether a subset can be formed whose sum is equal to the given target

    Args:
        array (list[int]): input array of integers
        target (int): target value to be achieved

    Returns:
        bool: returns True/False

    >>> subset_sum_bottom_up([1,5,11,15])
    True
    >>> subset_sum_bottom_up([1,5,3])
    False
    """
    array_sum = sum(array)
    if array_sum%2!=0: 
        return False
    else:
        target = array_sum//2
    t = [[False for _ in range(target+1)] for _ in range(len(array)+1)]

    for i in range(len(array)+1):
        for j in range(target+1):
            #if target is 0 then it can always be achieved
            if j==0:
                t[i][j] = True
            else:
                if array[i-1]<=j:
                    t[i][j] = t[i-1][j-array[i-1]] or t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
    return t[len(array)][target]

if __name__ == "__main__":
    import doctest
    doctest.testmod()