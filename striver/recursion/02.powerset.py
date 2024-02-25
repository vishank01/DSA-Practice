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
        for _ in range(2):
            out.append(array[n-1])
            helper(array,n-1,out)
            out.pop()#backtrack
        helper(array,n-1,out)
    print(f"All possible subsequences of given array {array} using backtracking are :");helper(array,len(array),[])

if __name__=="__main__":
    print_all_sub_sequences([1,2,3])
    print_all_sub_sequences_backtracking([1,2,3])