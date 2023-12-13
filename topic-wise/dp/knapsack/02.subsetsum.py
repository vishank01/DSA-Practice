"""// https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
Given a set of non-negative integers and a value sum, 
the task is to check if there is a subset of the given set whose sum is equal to the given sum. 

"""
def subset_sum_top_down(array:list[int],target:int)->bool:
    """Given set of non-negative integers and target value, function returns True/False based on
    whether a subset can be formed whose sum is equal to the given target

    Args:
        array (list[int]): input array of integers
        target (int): target value to be achieved

    Returns:
        bool: returns True/False

    >>> subset_sum_top_down([3, 34, 4, 12, 5, 2],9)
    True
    >>> subset_sum_top_down([3, 34, 4, 12, 5, 2],30)
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
    
    return helper(array,target,len(array))

def subset_sum_bottom_up(array:list[int],target:int)->bool:
    """Given set of non-negative integers and target value, function returns True/False based on
    whether a subset can be formed whose sum is equal to the given target

    Args:
        array (list[int]): input array of integers
        target (int): target value to be achieved

    Returns:
        bool: returns True/False

    >>> subset_sum_bottom_up([3, 34, 4, 12, 5, 2],9)
    True
    >>> subset_sum_bottom_up([3, 34, 4, 12, 5, 2],30)
    False
    """
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
    
if __name__=="__main__":
    import doctest
    doctest.testmod()
