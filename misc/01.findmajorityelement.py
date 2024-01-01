"""
https://www.enjoyalgorithms.com/blog/find-the-majority-element-in-an-array

Problem Statement: Find Majority Element in an Array

Difficulty: Medium, Asked-in: Microsoft, Google, Amazon, Yahoo.

Key Takeaways

    An excellent problem to learn problem-solving using various approaches and step-by-step time and space complexity optimization.
    The Boyer-Moore Voting algorithm is worth exploring, which uses fascinating insight from the problem to get the solution in O(n) time and O(1) space.
    
Let’s understand the problem

    You are given an array X[] consisting of n elements, write a program to find the majority element in an array i.e. return the number which appears more than n/2 times.

    Assume that array is non-empty and the majority element always exists.
    A majority element appears more than n/2 times, so there is at most one such element.
    
    Examples

        Input: X[] = [2, 12, 2, 2, 2, 4, 2], Output: 2

        Explanation: 2 is the majority element which appears 5 times.

        Input: A[]= [3, 3, 4, 2, 4, 4, 2, 4, 4], Output: 4

        Explanation: The frequency of 4 is 5 which is greater than half of the size of the array. 

        Input: X[] = [4, 3, 4], Output: 4

        Input: X[] = [1, 1, 1, 1, 1, 1], Output: 1

Discussed solution approaches

1. Brute force approach using nested loops
2. Using sorting
3. Using divide and conquer approach
4. Using hash table
5. Using bit manipulation approach
6. Using randomized algorithm
7. An efficient single loop solution using the Boyer-Moore voting algorithm

Comparisons of time and space complexities

    1. Two nested loops: Time = O(n^2), Space = O(1).
    2. Using sorting: Time = O(nlogn), Space = O(1).
    3. Divide and conquer: Time = O(nlogn), Space = O(1).
    4. Hash table: Time = O(n), Space = O(n).
    5. Bit manipulation: Time = O(n), Space= O(1).
    6. Randomized algorithm: Time = O(nlogn), with a probability of failure 1/n if n is very large, Space = O(1).
    7. Boyer-Moore voting algorithm: Time = O(n), Space = O(1).

"""

def find_majority_ele_by_brute_force(array:list[int])->int:
    n = len(array)
    for i in range(n):
        majority_cnt = 0 
        for j in range(n):
            if array[i]==array[j]:
                majority_cnt+=1
        if majority_cnt>n//2:
            return array[i]
    return -1

def find_majority_ele_by_sorting_approach(array:list[int])->int:
    array.sort()
    return array[len(array)//2]

def find_majority_ele_by_divide_and_conquer_approach(array:list[int])->int:
    """
        Divide step: 
            We divide the array into two equal halves by calculating the mid-value, i.e., mid = (low+high)/2.

        Conquer step: 
            We recursively calculate the majority element of the left and right halves and store them in variables leftMajority and rightMajority.
                leftMajority = find_majority_ele_by_divide_and_conquer_approach(array, low, mid)
                rightMajority = find_majority_ele_by_divide_and_conquer_approach(array, mid + 1, high)
        
        Combine step: 
            If the majority elements of the left and right halves are equal, then it must be the global majority element, and we return this value.
            Otherwise, we need to determine which one is the majority. To do this, we count the frequency of leftMajority and rightMajority in the input array.

        Base case: 
            This is the trivial case of a single-element array when both left and right ends are equal. We return this single element as the majority element, i.e., if (l == r), return X[l] or X[r].

        Solution analysis

            We are solving problem size n by recursively solving two smaller sub-problem of size n/2 and combing the solution of these two smaller problems by counting frequency of leftMajority and rightMajority.

                Time complexity of divide part = O(1).
                Time complexity of conquer part = 2T(n/2).
                Time complexity of combine part = Time complexity of counting the frequency of leftMajority + Time complexity of counting the frequency of rightMajority = O(n) + O(n) = O(n).
            
            Overall time complexity T(n) = O(1) + 2T(n/2) + O(n) = 2T(n/2) + O(n).
            So time complexity can be represented by the following recurrence relation:

                T(n) = 2T(n/2) + O(n), if n > 1
                T(n) = O(1), if n = 1
            We can use the master theorem or recursion tree method to solve this recurrence relation. If we observe closely, this is similar to merge sort recurrence. So time complexity = O(nlogn). 
            The above divide and conquer method does not explicitly allocate any additional memory, but it uses additional memory for call stack due to recursion. 
            
            The call stack size depends on the max depth of the recursion tree, which is O(logn). 
            Input size is decreasing by a factor of 2 at each recursive call (Think!). So space complexity = O(logn).

        Note: 
            This idea will only work if we assume that the majority element does not always exist.
            Why? Think about that! So here, if the majority element does not exist, we will return -1.
    """

    def count_freq_of_ele_in_sub_array(array:list[int],low:int,high:int,ele:int):
        cnt = 0
        for i in range(low,high+1):
            if array[i]==ele: cnt+=1
        return cnt

    def helper(array:list[int],low:int,high:int):
        if low==high:
            return array[low]
        mid = (low+high)//2
        left_majority_ele = helper(array,low,mid)
        right_majority_ele = helper(array,mid+1,high)

        if left_majority_ele==right_majority_ele:
            return left_majority_ele
        else:
            left_majority_ele_freq = count_freq_of_ele_in_sub_array(array,low,high,left_majority_ele)
            right_majority_ele_freq = count_freq_of_ele_in_sub_array(array,low,high,right_majority_ele)

            if left_majority_ele_freq>(high-low+1)//2:
                return left_majority_ele
            elif right_majority_ele_freq>(high-low+1)//2:
                return right_majority_ele
            else:
                return -1
            
    return helper(array,0,len(array)-1)


def find_majority_ele_by_randomized_algorithm(array:list[int])->int:
    """
        Solution idea

            In the given problem, more than n/2 elements are equal to the majority element. 
            So, if we choose some random element from the input, then there is more than a 50% probability that the chosen element will be the majority element. 
            If we perform this trial more and more, the chances of success will be higher.

            So, one basic idea would be to select a random element from the array and check whether it is the majority element or not. 
            If it is, we return that element. Otherwise, we repeat the process.

            There are some critical questions: 
                What is the exact probability that the algorithm will find the majority element? What is the time complexity of the algorithm? We will explore the answers to these questions in the analysis section.

        Solution analysis

            There are n choices for choosing an element and out of these choices, the chance of success is atleast n/2 + 1. Suppose every choice is equally likely, 
            then the probability of success is (n/2 + 1)/n = 1/2 + 1/n > 1/2 (for n > 0). In other words, the probability of failure is at most 1/2.

            To reduce the probability of failure, each time we make independent random choices and repeat the algorithm if we don't succeed. 
            If we repeat the algorithm 10 times, then the probability of failure is at most (1/2)^10.
            
            If we repeat the algorithm logn times, the probability of failure is at most (1/2)^logn = 1/(n^log 2) = 1/n. In other words, the algorithm succeeds with a high probability of at least (1 – 1/n).
            If n is very large, this algorithm can produce the majority element in O(nlogn) time with a high probability of success. Note: The time complexity of each trial is O(n). If we repeat the trial logn times
            If we repeat the algorithm n times, the probability of failure is at most (1/2)^n = 1/(2^n). In other words, the algorithm succeeds with a high probability, which is at least 1 – 1/(2^n).

            Time complexity is n*O(logn) = O(nlogn).
    """
    def count_frequency(array:list[int],n,ele:int):
        cnt = 0
        for i in range(n):
            if array[i]==ele: cnt+=1
        return cnt
    
    def get_random_index_in_range(start:int,end:int)->int:
        return random.randrange(start,end+1)
    
    n = len(array)
    attempts = 100
    while attempts>0:
        random_idx = get_random_index_in_range(0,n-1)
        if count_frequency(array,n,array[random_idx])>n//2:
            return array[random_idx]
        attempts-=1
    return -1

def find_majority_boyre_moore_voting_algorithm(array:list[int])->int:
    """
        Solution idea

            The intuition behind Boyer-Moore Voting algorithm:
                Since the majority element appears more than n/2 times, its frequency is greater than the combined frequency of all the other elements. 
                So, if we mark the occurrence of the majority element as +1 and the occurrence of any other element as -1, then the overall sum of these markings would definitely be greater than zero.

        Solution steps

            To keep track of our current guess of the majority element, we declare a variable majorityCandidate and maintain a counter variable count. Initially, the value of both variables is equal to 0.
            Let's walk across the array.
                1. If the current element matches our guess, we increment the count by 1. If the current element doesn't match our guess, we decrement the count by 1.
                2. If count == 0, we reset the current guess and make it equal to the current element, i.e., majorityCandidate = X[i]. In other words, we forget about everything up to the previous index and consider the current element as a potential candidate for the majority element.
                3. By the end of the loop, the value of the majority element gets stored in the variable majorityCandidate.
                4. There are many ways to think about why this algorithm works. One good intuition is to think of this algorithm as breaking the input into a chunk of consecutive copies of a particular value.

            Incrementing the counter corresponds to marking multiple copies of the same value.
            Decrementing the counter corresponds to some other sequences of values, "cancelling out" the accumulation of values of a particular type.

        Solution analysis

            We are running a single loop n time and performing a constant operation at each step of the iteration. 
            
            Time complexity = O(n). Space complexity = O(1), because we are using constant extra space.

        Note:
            As long as the majority element occurs with a frequency of at least n/2, we can guarantee that this approach will always find the majority element.
    """
    count = 0
    majority_ele = 0
    for i in range(len(array)):
        if count == 0:
            majority_ele = array[i]
        if array[i] == majority_ele:
            count = count + 1
        else:
            count = count - 1
    return majority_ele

if __name__=="__main__":
    import unittest;import random
    class TestSolution(unittest.TestCase):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.test_data = [
                {"input":([4,3,4]),"output":4},
                {"input":([1,1,1,1]),"output":1},
                {"input":([2, 12, 2, 2, 2, 4, 2]),"output":2},
                {"input":([3, 3, 4, 2, 4, 4, 2, 4, 4]),"output":4},
            ]

        def test_brute_force(self):
            for testcase in self.test_data:
                self.assertEqual(find_majority_ele_by_brute_force(testcase["input"]),testcase["output"])

        def test_sorting_approach(self):
            for testcase in self.test_data:
                self.assertEqual(find_majority_ele_by_sorting_approach(testcase["input"]),testcase["output"])

        def test_divide_and_conquer_approach(self):
            for testcase in self.test_data:
                self.assertEqual(find_majority_ele_by_divide_and_conquer_approach(testcase["input"]),testcase["output"])

        def test_random_algorithm_approach(self):
            for testcase in self.test_data:
                self.assertEqual(find_majority_ele_by_randomized_algorithm(testcase["input"]),testcase["output"])

        def test_boyer_moore_voting_algorithm(self):
            for testcase in self.test_data:
                self.assertEqual(find_majority_boyre_moore_voting_algorithm(testcase["input"]),testcase["output"])

    unittest.main()
