from typing import Any

class RecursionUtil:
    def __init__(self):
        print("\n\n"+"*"*10+"ReverseUsingRecursion"+"*"*10+"\n")
        print(f"2 power 3 is {self.power(2,3)}")
        print(f"5 power 4 is {self.power(2,3)}")
        print(f"5+9 is {self.add(5,9)}")
        print(f"20th Fibanocci Number is {self.fib(20)}")
        print(f"GCD of 8 and 6 is {self.gcd_decrease_and_conquer(8,6)}")
        print(f"GCD of 8 and 6 using Euclidean Algorithm is {self.gcd_by_euclidean_algorithm(8,6)}")
        print("\n\n"+"*"*20+"\n")

    def power(self,a:int|float,b:int|float)->int|float:
        if b==0:
            return 1
        return a*self.power(a,b-1)

    def add(self,a:int|float,b:int|float)->int|float:
        if b==0:
            return a
        return 1+self.power(a,b-1)
    
    def fib(self,n:int)->int:
        """finds nth fibanocci both fib calls can call with same inputs in their respective trees so memoization will improve the speed"""
        if n<=1: return n
        return self.fib(n-1)+self.fib(n-2)
    
    def gcd_decrease_and_conquer(self,a:int,b:int)->int:
        """
            Proof that GCD(A,B)=GCD(A,A-B)
            This is one of the best problems to learn problem-solving using Recursion (Decrease and Conquer Strategy)

            Note: 
                1. if a=0 then GCD(a,b)=b 
                2. If a=0 and b=0 GCD(a,b) is Undefined
                3. If smaller of the two divides the other number, then GCD is smallest number otherwise GCD is smaller than smallest number
                4. GCD(A,B) evenly divides C where (C=A-B)
                    The GCD(A,B), by definition, evenly divides A. As a result, A must be some multiple of GCD(A,B). i.e. X⋅GCD(A,B)=A where X is some integer
                    The GCD(A,B), by definition, evenly divides B. As a result,  B must be some multiple of GCD(A,B). i.e. Y⋅GCD(A,B)=B where Y is some integer
                    A-B=C gives us:
                        X⋅GCD(A,B) - Y⋅GCD(A,B) = C
                        (X - Y)⋅GCD(A,B) = C

        """
        if b==0: return a
        return self.gcd_decrease_and_conquer(b,a-b) if a>b else self.gcd_decrease_and_conquer(a,b-a)
    
    def gcd_by_euclidean_algorithm(self,a:int,b:int)->int:
        """The algorithm is based on the fact that if r is the remainder when a is divided by b, then gcd(a,b) = gcd(b,r).
        
            Euclidean Algorithm Analysis:
            
                dividend = divisor*quotient + remainder

                GCD(a,b)=GCD(b,a-b)=GCD(a-b,b)=GCD(a-2b,b)=GCD(a-3b,b)=GCD(a-Qb,b) = GCD(r,b) = GCD(b,r)

            Example:
                GCD(48,18) = GCD(18,48%18) = GCD(18,12)
                GCD(18,12) = GCD(12,6)
                GCD(12,6) = GCD(6,0) = 6
        """
        if b==0: return a
        return self.gcd_by_euclidean_algorithm(b,a%b)
            

class ReverseUsingRecursion:
    def __init__(self):
        print("\n\n"+"*"*10+"ReverseUsingRecursion"+"*"*10+"\n")
        print(f"Reverse of string hello using recursion is {self.reverse_string('hello')}")
        print(f"Reverse of string hello world! using divide and conquer is {self.reverse_string_divide_and_conquer('hello world!')}")
        print(f"Reverse of an array [1,2,3,4,5] using swap+recursion is {self.reverse_array_using_swap([1,2,3,4,5])}")
        print("\n\n"+"*"*20+"\n")

    def reverse_string(self,string:str)->str:
        
        def helper(string:str,n:int)->str:
            if n==0: return string[0]
            return string[n]+helper(string,n-1)
        
        return helper(string,len(string)-1)

    def reverse_array_using_swap(self,array:list[Any])->list[Any]:
        
        def helper(array:list[Any],low:int,high:int)->list[Any]:
            if low>=high: return array
            array[low],array[high] = array[high],array[low]
            return helper(array,low+1,high-1)

        return helper(array,0,len(array)-1)


    def reverse_string_divide_and_conquer(self,string:str)->str:
        def helper(string:str,low:int,high:int)->str:
            if low==high: return string[low]

            mid = (low+high)//2

            return helper(string,mid+1,high)+helper(string,low,mid)

        return helper(string,0,len(string)-1)

if __name__=="__main__":
    RecursionUtil()
    ReverseUsingRecursion()


