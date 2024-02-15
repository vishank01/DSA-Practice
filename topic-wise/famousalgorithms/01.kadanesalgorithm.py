"""
https://medium.com/enjoy-algorithm/find-maximum-subarray-sum-882aeb5b76f6#:~:text=Now%2C%20we%20can%20recursively%20find,array%20that%20crosses%20the%20midpoint.

Problem Statement:
    Largest Sum Contiguous Subarray (Kadane's Algorithm)

    Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 

Solution:
    The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far, 
    Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_so_far.


"""

def max_sum_subarray_brute_force(array:list[int]):
    """
    >>> max_sum_subarray_brute_force([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    n = len(array)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i,n):
            max_sum = max(max_sum,sum(array[i:j+1]))
    return max_sum

def max_sum_subarray_brute_force_optimied(array:list[int]):
    """
    >>> max_sum_subarray_brute_force_optimied([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    n = len(array)
    max_sum = float('-inf')
    for i in range(n):
        subarray_sum = 0
        for j in range(i,n):
            subarray_sum +=array[j]
            max_sum = max(max_sum,subarray_sum)
    return max_sum

def max_sum_subarray_divide_and_conquer(array:list[int]):
    """
    The maximum sub-array sum can only exist in three possible places:
        . In the left sub-array array[l…mid].
        . In the right sub-array array[mid+1…r].
        . In a sub-array that crosses the mid-point (l ≤ i ≤ mid ≤ j ≤ r) 
            i.e. it contains elements from both the left and right sub-arrays.
    >>> max_sum_subarray_divide_and_conquer([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    def find_max_crossing_sum(arr:list[int],l:int,m:int,h:int):
        sm = 0
        left_sum = right_sum = float('-inf')
        #direction of calc is from mid to left and mid to right (from mid towards both ends)
        for i in range(m, l-1, -1): 
            sm = sm + arr[i] 
            left_sum = max(left_sum,sm)
        # Include elements on right of mid 
        sm = 0
        for i in range(m+1, h + 1): 
            sm = sm + arr[i] 
            right_sum = max(right_sum,sm)
        return left_sum+right_sum
    
    def helper(array:list[int],left:int,right:int):
        if left==right: return array[left]
        mid = (left+right)//2
        left_sum = helper(array,left,mid)
        right_sum = helper(array,mid+1,right)
        crossing_sum = find_max_crossing_sum(array,left,mid,right)
        return max(left_sum,right_sum,crossing_sum)

    return helper(array,0,len(array)-1)

def max_sum_subarray_dynamic_programming(array:list[int]):
    """
    >>> max_sum_subarray_dynamic_programming([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    n = len(array)
    max_sum_ending_at_i = [0]*n
    max_sum_ending_at_i[0]=array[0]
    for i in range(1,n):
        max_sum_ending_at_i[i] = max(max_sum_ending_at_i[i],max_sum_ending_at_i[i-1]+array[i])
    return max(max_sum_ending_at_i)

def max_sum_subarray_using_kadanes_algo(array:list[int]):
    """
    >>> max_sum_subarray_using_kadanes_algo([-2, -3, 4, -1, -2, 1, 5, -3])
    7
    """
    curr_sum = 0
    max_sum = float('-inf')
    for i in range(len(array)):
        curr_sum = max(curr_sum+array[i],array[i])
        max_sum = max(curr_sum,max_sum)
    return max_sum

def max_sum_subarray_recursion(array:list[int]):
    def helper(array:list[int],n:int,start:int,end:int):
        if end == n:
            return
        elif start > end:
            return helper(array,n,start,end+1)
        else:
            print(array[start:end+1])
            return helper(array,n,start+1,end)
    return helper(array,len(array),0,len(array)-1)

def max_sum_sub_sequence(array:list[int]):
    """
        Here find all positive elements and return sum of them
        otherwise return maximum number (in case all elements are negative)
    """
    """
    >>> max_sum_sub_sequence([ -2, 11, -4, 2, -3, -10 ])
    29
    """
    max_sum = 0
    max_ele = max(array)
    if max_ele<=0: return max_ele
    for i in range(len(array)):
        if array[i]>0:
            max_sum+=array[i]
    return max_sum

if __name__=="__main__":
    import doctest
    doctest.testmod()