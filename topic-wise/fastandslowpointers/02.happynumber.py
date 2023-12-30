"""
Problem Statement: Happy Number

    Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
    
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.
 

Example 1:

    Input: n = 19
    Output: true
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Example 2:

    Input: n = 2
    Output: false
 

Constraints:

    1 <= n <= 231 - 1
"""

def get_square_sum(number:int)->int:
    ans = 0
    while number>0:
        digit = number%10
        ans += digit**2
        number = number//10
    return ans

def is_happy(number:int)->bool:
    """
        Approach:
            1. We saw in the LinkedList Cycle problem that we can use the Fast & Slow pointers method to find a cycle among a set of elements. 
            2. As we have described above, each number will definitely have a cycle. Therefore, we will use the same fast & slow pointer strategy to find the cycle.
            3. Once the cycle is found, we will see if the cycle is stuck on number 1 to find out if the number is happy or not.
    """
    slow_ptr = fast_ptr = number
    while True:
        #moves 1 step
        slow_ptr = get_square_sum(slow_ptr)
        #1 step ahead of slow_ptr (moves 2 steps)
        fast_ptr = get_square_sum(get_square_sum(fast_ptr))
        if slow_ptr==fast_ptr:
            break
    return slow_ptr==1

if __name__=="__main__":
    print(is_happy(19))
    # print(is_happy(2))