def print_name_n_times(name:str,n:int):
    """
    Time Complexity: O(N) 
        Since the function is being called n times, and for each function, we have only one printable line that takes O(1) time, so the cumulative time complexity would be O(N).
    Space Complexity: O(N) 
        In the worst case, the recursion stack space would be full with all the function calls waiting to get completed and that would make it an O(N) recursion stack space.
    """
    if n==0: return
    print(name,end=" ")
    print_name_n_times(name,n-1)

def print_1_n(n:int):
    if n==0: return
    print_1_n(n-1)
    print(n,end="")

def print_n_1(n:int):
    if n==0: return
    print(n,end="")
    print_n_1(n-1)

def sum_first_n_natural_numbers_functional_way(n:int):
    if n==0: return 0
    return n+sum_first_n_natural_numbers_functional_way(n-1)

def sum_first_n_natural_numbers_parameterized_way(n:int,sum:int=0):
    if n==0: return sum
    return sum_first_n_natural_numbers_parameterized_way(n-1,sum+n)

def factorial(n:int):
    def factorial_recursive(n:int):
        """Time Complexity: O(n); Space Complexity: O(n)"""
        if n==1: return 1
        return n*factorial_recursive(n-1)
    
    def factorial_iterative(n:int):
        """Time Complexity: O(n); Space Complexity: O(1)"""
        fact=1
        for i in range(2,n+1): fact*=i
        return fact
    print(f"Factorial of 5 using recursion approach is {factorial_recursive(5)}")
    print(f"Factorial of 5 using iterative approach is {factorial_iterative(5)} ")

def reverse_given_array(array:list[int]):
    def reverse_array_two_pointers(array:list[int]):
        i,j=0,len(array)-1
        while i<j:
            array[i],array[j]=array[j],array[i]
            i+=1;j-=1
        return array
    
    def reverse_array_using_swap_recursion(array:list[int],low:int,high:int)->list[int]:
        if low>=high: return array
        array[low],array[high] = array[high],array[low]
        return reverse_array_using_swap_recursion(array,low+1,high-1)

    def reverse_array_using_divide_and_conquer(array:list[int],low:int,high:int):
        if low>=high: return [array[low]]
        mid = (low+high)//2
        left_array = reverse_array_using_divide_and_conquer(array,low,mid)
        right_array = reverse_array_using_divide_and_conquer(array,mid+1,high)
        return right_array+left_array
    
    print(f"Reversal of array {array} using two pointers is {reverse_array_two_pointers(array)}")
    print(f"Reversal of array {array} using divide and conquer is {reverse_array_using_divide_and_conquer(array,0,len(array)-1)}")
    print(f"Reverse of array {array} using swap+recursion is {reverse_array_using_swap_recursion(array,0,len(array)-1)}")

def check_palindrome(string:str):
    def check_palindrome_recursion(string:str,low:int,high:int):
        if low>=high: return True
        return string[low]==string[high] and check_palindrome_recursion(string,low+1,high-1)
    
    print(f"Given String {string} is palindrome? : {check_palindrome_recursion(string,0,len(string)-1)}")

def nth_fibanocci(n:int):
    def nth_fibanocci_recursion(n:int):
        """
            Time Complexity: O(2^N) 
                This problem involves two function calls for each iteration which further expands to 4 function calls and so on which makes worst-case time complexity to be exponential in nature.
            Space Complexity: O(N) 
                At maximum there could be N function calls waiting in the recursion stack since we need to calculate the Nth Fibonacci number for which we also need to calculate (N-1) Fibonacci numbers before it.
        """
        if n<=1: return n
        return nth_fibanocci_recursion(n-1)+nth_fibanocci_recursion(n-2)
    
    print(f"Fibanocci of {n}th element is {nth_fibanocci_recursion(n)}")

if __name__=="__main__":
    print_name_n_times("vishnu",5);print("\n")
    print_1_n(5);print("\n")
    print_n_1(5);print("\n")
    print(f"Sum of First 5 Natural Numbers is :{sum_first_n_natural_numbers_functional_way(5)}")
    print(f"Sum of First 5 Natural Numbers is :{sum_first_n_natural_numbers_parameterized_way(5)}")
    factorial(5)
    reverse_given_array([1,2,3,4,5])
    check_palindrome("ABAA")
    nth_fibanocci(5)