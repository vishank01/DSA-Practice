"""

    ●   Place a queen arbitrarily at any position on the chessboard.
    ●   Check if this position is safe, i.e it is not attacked by any other queens.
    ●   If the position is not safe, then look for other positions on the board and if no 
        such position is found,then return false as we cannot place any more queens
    ●   If the position is safe, then recursively check for Q-1 queens, if the function
        returns true, in other words, all queens were placed successfully on the board,
        then return true.

    > Check if the position at x,y is not attacked by any other queen.
    > Check if no position is marked 1 in the same row.
    > Check if no position is marked 1 in the same column.
    > Check if no position is marked 1 in the diagonals.
    
"""

def place_n_queens(array:list[list],n:int,q:int)->str:
    """Places q queens on a given array of size n and returns positions of placed queens 
    and if no queens could be placed, it will return empty string

    Args:
        array (list[list]): input array on which queens will be placed
        n (Annotated[int,&quot;Size of Array&quot;]): size of input array
        q (Annotated[int,&quot;Number of Queens&quot;]): number of queens to be placed

    Returns:
        str: positions of queens which are placed on array, returns empty string if queens cannot be placed

    >>> place_n_queens([1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]],5,5)
    (0,0),(1,2),(2,4),(3,1),(4,3)
    >>> place_n_queens([1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]],5,3)
    (0,0),(1,2),(2,4)
    """
    def is_valid(array:list[list],n:int,row:int,column:int)->bool:
        """checks if given position in an array of size n is valid move for queen

        Args:
            array (list[list]): input array 
            n (int): size of input array
            row (int): row to be checked on given array
            column (int): column to be checked on given array

        Returns:
            bool: returns True/False based on a valid move
        """
        if row<0 or row>=n: return False
        if column<0 or column>=n: return False
        if array[row][column]==1: return False
        i=0
        while i<n:
            #check every row in with specific column
            if array[i][column]==1:
                return False
            i+=1
        j=0
        while j<n:
            #check every column with specific row
            if array[row][j]==1:
                return False
            j+=1
        i,j=row,column
        while 0<=i<n and 0<=j<n:
            #check diagonally top left
            if array[i][j]==1:
                return False
            i-=1
            j-=1
        i,j=row,column
        while 0<=i<n and 0<=j<n:
            #check diagonally bottom left
            if array[i][j]==1:
                return False
            i+=1
            j-=1
        i,j=row,column
        while 0<=i<n and 0<=j<n:
            #check diagonally top right
            if array[i][j]==1:
                return False
            i-=1
            j+=1
        i,j=row,column
        while 0<=i<n and 0<=j<n:
            #check diagonally bottom right
            if array[i][j]==1:
                return False
            i+=1
            j+=1
        return True
    
    def helper(array:list[list],n:int,q:int,current_queen_positions:list[str])->str:
        """Helper function to place given q queens on an array of size n

        Args:
            array (list[list]): input array where q queens to be placed
            n (int): size of input array
            q (int): number of queens to be placed in a given array
            current_queen_positions (list[str]): stores queen positions for every recursive call 
            and uses this in base condition to return queen positions

        Returns:
            str: positions of queens which are placed on array, returns empty string if queens cannot be placed
        """
        #base case
        if q==0:
            return ",".join(current_queen_positions)
        for i in range(n):
            for j in range(n):
                if is_valid(array,n,i,j):
                    array[i][j]=1
                    current_queen_positions.append(f"({i},{j})")
                    if helper(array,n,q-1,current_queen_positions):
                        return ",".join(current_queen_positions)
                    #backtrack
                    #only pass by reference mutable objects are backtracked. q will automatically be reverted back
                    array[i][j]=0
        return ",".join(current_queen_positions)

    return helper(array,n,q,current_queen_positions=list())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    n=5
    array = [[0 for _ in range(n)] for _ in range(n)]
    print(place_n_queens(array,n,3))