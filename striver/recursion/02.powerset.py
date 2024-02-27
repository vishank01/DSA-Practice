def sub_sequences_brute_force(array:list[int]):
    ans = []
    n = len(array)
    for i in range(n):
        for j in range(i,n):
            ans.append(array[i:j+1])
    return ans

def print_all_sub_sequences(array:list[int]):
    """
        Time Complexity: O(2^n)
        Space Complexity: O(n), Recursion stack.
        Approach:
            Draw a recursion tree with ip/op approach with op
            At every point we have two choices, include character/don't include
    """
    out = []
    def helper(array:list[int],n:int,out:list[int]):
        """Use last element to decide whether to include/don't include"""
        if n==0: print(out);return
        helper(array,n-1,[array[n-1]]+out)
        helper(array,n-1,out)#don't incldue

    print(f"All possible subsequences of given array {array} are :");helper(array,len(array),out)

def print_all_sub_sequences_backtracking(array:list[int]):
    def helper(array:list[int],n:int,out:list[int]):
        if n==0: print(out);return
        #two choices for every move
        out.append(array[n-1])
        helper(array,n-1,out)
        out.pop()#backtrack
        helper(array,n-1,out)
    print(f"All possible subsequences of given array {array} using backtracking are :");helper(array,len(array),[])

def subsets_bit_manipulation(nums:list[int]):
    """
        Time Complexity: 2^N*N
            To remove addition N, Recursion is useds
    """
    n = len(nums)
    ans = []
    #1<<n is same as 2**n
    for combination_number in range(1<<n):
        ds = []
        for i in range(n):
            ##1<<i checks for presence of 1 in all possible n locations of given num
            if combination_number &(1<<i):
                ds.append(nums[i])
        ans.append(ds)
    return ans

if __name__=="__main__":
    print_all_sub_sequences([1,2,3])
    print_all_sub_sequences_backtracking([1,2,3])
    print(f"All subsets using bit-manipulation approach is {subsets_bit_manipulation([1,2,3])}")
    print(f"All subsets using brute-force approach is {sub_sequences_brute_force([1,2,3])}")