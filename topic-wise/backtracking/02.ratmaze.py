def searchMaze(arr:list[list[int]],n:int)->str:
    """Find a possible solution for RAT to go from Source to Destination

    Args:
        arr (list[list[int]]): input 2D array of integers with 0 representing blocked and 1 means available
        n (int): size of input squared array 5 means 5x5 matrix

    Returns:
        str: outputs format like DRDRR
    >>> searchMaze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4)
    'DDRDRR'
    >>> searchMaze([[1,0],[1,0]],2)
    ''
    """
    output = []
    if arr[0][0] == 0:
        return output
    searchMazeHelper(arr,n,0,0,output)
    return "".join(output)

def is_safe(arr:list[list],n:int,i:int,j:int):
    if 0<=i<n and 0<=j<n and arr[i][j]==1:
        return True

def searchMazeHelper(arr:list[list],n:int,i:int,j:int,output:list,current_path=""):
    if i==n-1 and j==n-1:
        output.append(current_path)
    else:
        if is_safe(arr,n,i+1,j):
            #move down
            arr[i+1][j]=0
            searchMazeHelper(arr,n,i+1,j,output,current_path+"D")
        if is_safe(arr,n,i,j+1):
            #move right
            arr[i][j+1]=0
            searchMazeHelper(arr,n,i,j+1,output,current_path+"R")
        if is_safe(arr,n,i-1,j):
            #move top
            arr[i-1][j]=0
            searchMazeHelper(arr,n,i-1,j,output,current_path+"T")
        if is_safe(arr,n,i,j-1):
            #move left
            arr[i][j-1]=0
            searchMazeHelper(arr,n,i,j-1,output,current_path+"L")
        #mark as available so that all other paths will be found
        arr[i][j]=1

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    print(searchMaze([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4))