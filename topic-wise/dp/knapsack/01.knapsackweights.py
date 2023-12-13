"""
    Problem Statement:
        Given a knapsack with capacity C and two arrays w[] and val[] representing the weights 
        and values of N distinct items, the task is to find the maximum value you can put into the knapsack. 
        Items cannot be broken and an item with weight X takes X capacity of the knapsack.
"""

def knapsack_weights_recursion(weights:list[int],values:list[int],capacity:int)->int:
    """ Given weights and values array with knapsack capacity, returns maximum value that can be put in knapsack

        Time Complexity: 
            T(N) = 2T(N-1) + O(1), which is simplified to O(2^N).

    Args:
        weights (list[int]): weights array
        values (list[int]): corresponding values array for given weights
        capacity (int): capacity of knapsack

    Returns:
        int: maximum value that is put on to the knapsack

    >>> knapsack_weights_recursion([3,4,5],[30, 50, 60],8)
    90
    >>> knapsack_weights_recursion([10000],[10],100000)
    10
    """

    def helper(weights:list[int],values:list[int],capacity:int,n:int):
        """helper function to find maximum value that fits in knapsack

        Args:
            weights (list[int]): weights array
            values (list[int]): corresponding values array for given weights
            capacity (int): capacity of knapsack
            n (int): size of weights array

        Returns:
            int: maximum value that is put on to the knapsack
        """
        #for base condition we need to think of the smallest valid input that we can pass 
        #weights array size (n) can be atleast 0 or min weight (capacity) can be 0 but not negetive;
        if n==0 or capacity==0:
            return 0
        else:
            if weights[n-1]<=capacity:
                return max(helper(weights,values,capacity-weights[n-1],n-1)+values[n-1],helper(weights,values,capacity,n-1),)
            else:
                return helper(weights,values,capacity,n-1)
            
    return helper(weights,values,capacity,len(weights))

def knapsack_weights_top_down_memoization(weights:list[int],values:list[int],capacity:int)->int:
    """ Given weights and values array with knapsack capacity, returns maximum value that can be put in knapsack

    This uses memoization to speedup process by avoiding recalculating repeated tasks using temporary structure t

    Args:
        weights (list[int]): weights array
        values (list[int]): corresponding values array for given weights
        capacity (int): capacity of knapsack

    Returns:
        int: maximum value that is put on to the knapsack

    >>> knapsack_weights_top_down_memoization([3,4,5],[30, 50, 60],8)
    90
    >>> knapsack_weights_top_down_memoization([10000],[10],100000)
    10
    """
    
    #temp array will store variables that change in recursion which are values(n) and capacity
    #always columns will be in inner for loop
    t =[[-1 for _ in range(capacity+1)] for _ in range(len(values)+1)]

    def helper(weights:list[int],values:list[int],capacity:int,n:int):
        """helper function to find maximum value that fits in knapsack

        Args:
            weights (list[int]): weights array
            values (list[int]): corresponding values array for given weights
            capacity (int): capacity of knapsack
            n (int): size of values array

        Returns:
            int: maximum value that is put on to the knapsack
        """
        #for base condition we need to think of the smallest valid input that we can pass 
        #weights array size (n) can be atleast 0 or min weight (capacity) can be 0 but not negetive;

        if n==0 or capacity==0:
            return 0
        if t[n][capacity]!=-1:
            return t[n][capacity]
        if weights[n-1]<=capacity:
            t[n][capacity] = max(helper(weights,values,capacity-weights[n-1],n-1)+values[n-1],helper(weights,values,capacity,n-1),)
        else:
            t[n][capacity] = helper(weights,values,capacity,n-1)
        return t[n][capacity]
            
    return helper(weights,values,capacity,len(values))

def knapsack_weights_bottom_up(weights:list[int],values:list[int],capacity:int)->int:
    """ Given weights and values array with knapsack capacity, returns maximum value that can be put in knapsack
        Top down approach uses pre-defined array to populate from start to end and doesn't use recursion
        Advantages:
            >   Space complexity is better compared to recursion as it doesn't require to store recursive call stacks

    Args:
        weights (list[int]): weights array
        values (list[int]): corresponding values array for given weights
        capacity (int): capacity of knapsack

    Returns:
        int: maximum value that is put on to the knapsack

    >>> knapsack_weights_bottom_up([3,4,5],[30, 50, 60],8)
    90
    >>> knapsack_weights_bottom_up([10000],[10],100000)
    10
    """
    #temp array will store variables that change in recursion which are values(n) and capacity
    t =[[0 for _ in range(capacity+1)] for _ in range(len(values)+1)]
    for i in range(len(values)+1):
        for j in range(capacity+1):
            if i==0 or j==0:
                t[i][j] = 0
            else:
                if weights[i-1]<=j:
                    t[i][j] = max(t[i-1][j-weights[i-1]]+values[i-1],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
    return t[len(values)][capacity]
            
if __name__=="__main__":
    import doctest
    doctest.testmod()
    # knapsack_weights_memoization([10000],[10],100000)