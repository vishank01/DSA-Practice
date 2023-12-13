available_directions = [("D",1,0),("R",0,1),("T",-1,0),("L",0,-1)]

"""
    format for backtracking algorithm is 
    def backtracking_example(arr,n,r+n_r,c+n_c,output,current_path):
        if is_finish():
            pass
        else:
            #loop over all possible directions
            for _ in range(n):
                #check if that direction is valid
                if is_valid():
                    #set some variable
                    arr[r][c]=-1
                    current_path += d
                    backtracking_example(arr,n,r+n_r,c+n_c,output,current_path)
                    #backtrack revert it
                    arr[r+n_r][c+n_c] = 1
                    current_path = current_path[:-1]
"""

def find_all_possible_solutions_for_maze(arr:list[list[int]],n:int)->str:
    """Find all possible solutions for RAT to go from Source to Destination

    Args:
        arr (list[list[int]]): input 2D array of integers with 0 representing blocked and 1 means available
        n (int): size of input squared array 5 means 5x5 matrix

    Returns:
        str: outputs format like DDRDRR DRDDRR
    >>> find_all_possible_solutions_for_maze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4)
    'DDRDRR DRDDRR'
    >>> find_all_possible_solutions_for_maze([[1,0],[1,0]],2)
    ''
    """

    def is_safe(arr:list[list],n:int,r:int,c:int):
        if 0<=r<n and 0<=c<n and arr[r][c]==1:
            return True

    def helper(arr:list[list],n:int,r:int,c:int,output:list,current_path=""):
        if r==n-1 and c==n-1:
            output.append(current_path)
            output.append(" ")
        else:
            for d,n_r,n_c in available_directions:
                if is_safe(arr,n,r+n_r,c+n_c):
                    #-1 is occupied by our move 
                    arr[r][c]=-1
                    current_path += d
                    helper(arr,n,r+n_r,c+n_c,output,current_path)
                    #backtrack
                    arr[r+n_r][c+n_c] = 1
                    current_path = current_path[:-1]
    output = []
    if arr[0][0] == 0:
        return output
    helper(arr,n,0,0,output)
    return "".join(output).strip()

def find_any_possible_solutions_for_maze(arr:list[list[int]],n:int)->str:
    """Find any possible solutions for RAT to go from Source to Destination

    Args:
        arr (list[list[int]]): input 2D array of integers with 0 representing blocked and 1 means available
        n (int): size of input squared array 5 means 5x5 matrix

    Returns:
        str: outputs format like DDRDRR
    >>> find_any_possible_solutions_for_maze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4)
    'DDRDRR'
    >>> find_any_possible_solutions_for_maze([[1,0],[1,0]],2)
    ''
    """

    def is_safe(arr:list[list],n:int,r:int,c:int):
        if 0<=r<n and 0<=c<n and arr[r][c]==1:
            return True

    def helper(arr:list[list],n:int,r:int,c:int,output:list,current_path=""):
        if r==n-1 and c==n-1:
            output.append(current_path)
            output.append(" ")
            return True
        else:
            for d,n_r,n_c in available_directions:
                if is_safe(arr,n,r+n_r,c+n_c):
                    #-1 is occupied by our move 
                    arr[r][c]=-1
                    current_path += d
                    if helper(arr,n,r+n_r,c+n_c,output,current_path):
                        return True
                    #backtrack
                    arr[r+n_r][c+n_c] = 1
                    current_path = current_path[:-1]
            return False
    output = []
    if arr[0][0] == 0:
        return output
    helper(arr,n,0,0,output)
    return "".join(output).strip()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # print(find_all_possible_solutions_for_maze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4))
    # print(find_any_possible_solutions_for_maze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4))