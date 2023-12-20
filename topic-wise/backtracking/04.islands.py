"""Given a binary 2D matrix, find the number of islands. A group of connected 1s forms an island. 
For example, the below matrix contains 4 islands.

Input: mat[][] = {
    {1, 1, 0, 0, 0},
    {0, 1, 0, 0, 1},
    {1, 0, 0, 1, 1},
    {0, 0, 0, 0, 0},
    {1, 0, 1, 0, 0}
}
Output: 4

The idea is to keep an additional matrix to keep track of the visited nodes in the given matrix, 
and perform DFS to find the total number of islands

"""

def count_islands(matrix:list[list[int]])->int:
    cnt=0
    available_moves = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

    def is_valid_x_y(i:int,j:int)->bool:
        if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]==1:
            return True

    def dfs(i:int,j:int)->int:
        matrix[i][j]=-1
        for current_move in available_moves:
            i,j = i+current_move[0],j+current_move[1]   
            if is_valid_x_y(i,j):
                dfs(i,j)
            i,j=i-current_move[0],j-current_move[1]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                cnt+=1
                dfs(i,j)
    return cnt


if __name__=="__main__":
    graph = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    no_of_islands = count_islands(graph)
    assert no_of_islands==5
    print(f"Number of islands {no_of_islands}")