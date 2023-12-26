"""
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1128880643

Problem Statement: Squaring a Sorted Array

"""

def square_sorted_array_straight_forward_approach(nums:list[int])->list[int]:
    """
        Time Complexity: N+O(NLogN) -> because sort is used
        Space Complexity: O(N)
    """
    output = []
    for i in range(len(nums)):
        output.append(nums[i]*nums[i])
    output.sort()
    return output

def square_sorted_array_two_pointer_approach(nums:list[int])->list[int]:
    """
        Approach:

            1. Since the numbers at both ends can give us the largest square, an alternate approach could be to use two pointers starting at both ends of the input array. 
            2. At any step, whichever pointer gives us the bigger square, we add it to the result array and move to the next/previous number according to the pointer.
        
        Time Complexity: O(N) 
        Space Complexity: O(N)
    """
    n = len(nums)
    #to store result
    output = [None for _ in range(n)]
    i,j,highest_idx = 0,n-1,n-1
    while i<=j:
        n1,n2 = nums[i]**2,nums[j]**2
        if n1>n2:
            output[highest_idx] = n1
            i+=1
        else:
            output[highest_idx] = n2
            j-=1
        highest_idx-=1
    return output
    

    

if __name__=="__main__":
    print(square_sorted_array_two_pointer_approach([-2, -1, 0, 2, 3]))
    print(square_sorted_array_two_pointer_approach([-3, -1, 0, 1, 2]))