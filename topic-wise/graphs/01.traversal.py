"""
Breadth-First Traversal (or Search) for a graph is similar to the Breadth-First Traversal of a tree.

The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we divide the num_vertices into two categories:

Visited and
Not visited.

How does BFS work?
Starting from the root, all the nodes at a particular level are visited first and then the nodes of the next level are traversed till all the nodes are visited.

To do this a queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue and the nodes of the current level are marked visited and popped from the queue.
"""

class Graph:
    def __init__(self,num_vertices:int) -> None:
        """Implementation of BFS using Adjacency Matrix to traverse from a given source vertex
            Time Complexity:
                Addition of node is O(1)
                Removal of node is O(1)
                Initialization is O(N*N)

        Args:
            v (int): number of num_vertices for a graph
        """
        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]

    def add_edge(self,v1:int,v2:int)->None:
        if v1<self.num_vertices and v2<self.num_vertices:
            self.graph[v1][v2]=1
            self.graph[v2][v1]=1

    def remove_edge(self,v1:int,v2:int)->None:
        if v1<self.num_vertices and v2<self.num_vertices:
            self.graph[v1][v2]=0
            self.graph[v2][v1]=0

    def remove_all_edges(self)->None:
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                self.graph[i][j]=0
    
    def print_graph(self):
        for row in self.graph:
            for val in row:
                print('{:4}'.format(val),end="")
            print("\n")

    def bfs(self,start_vertex:int)->None:
        """BFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)
        """
        print(f"\nFollowing is Breadth First Traversal from source vertex {start_vertex}")
        if start_vertex<self.num_vertices:
            queue = []
            visited = [False for _ in range(self.num_vertices)]
            
            queue.append(start_vertex)
            visited[start_vertex] = True

            while len(queue)>0:
                current_vertex = queue.pop(0)
                print(current_vertex,end=' ')
                #loop over vertex's row and get it's adjacent vertices
                for i in range(self.num_vertices):
                    if (self.graph[current_vertex][i] == 1 and (not visited[i])):
                        # print(i,j,self.graph[i])
                        queue.append(i)
                        visited[i]=True

    def dfs(self,start_vertex:int,visited=None)->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)
        """
        if visited is None:
            print(f"\nPrinting DFS using Recursive Approach from source vertex {start_vertex}")
            visited = [False for _ in range(self.num_vertices)]
        if start_vertex<self.num_vertices:
            visited[start_vertex] = True
            print(start_vertex,end=" ")
            for i in range(self.num_vertices):
                if (self.graph[start_vertex][i] == 1 and (not visited[i])):
                    self.dfs(i,visited)

    def dfs_iterative(self,start_vertex:int)->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)

        Limitations:
            Iterative DFS mplementation prints only vertices that are reachable from a given vertex. 
            To print all vertices of a graph, call DFS for every unvisited vertex.
        """
        print(f"\nFollowing is Depth First Traversal from source vertex {start_vertex}")
        if start_vertex<self.num_vertices:
            stack = []
            visited = [False for _ in range(self.num_vertices)]
            
            stack.append(start_vertex)
            visited[start_vertex] = True

            while len(stack)>0:
                current_vertex = stack.pop(-1)
                print(current_vertex,end=' ')
                #loop over vertex's row and get it's adjacent vertices
                for i in range(self.num_vertices):
                    if (self.graph[current_vertex][i] == 1 and (not visited[i])):
                        # print(i,j,self.graph[i])
                        stack.append(i)
                        visited[i]=True

if __name__=="__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 4)
    g.print_graph()

    # bfs(2) is 2 0 1 3 4
    g.bfs(2)
    # bfs(1) is 1 0 2 3 4
    g.bfs(1)
    # bfs(0) is 0 1 2 3 4
    g.bfs(0)

    g.dfs_iterative(0)
    g.dfs(0)

    # g.remove_all_edges()
    # g.add_edge(1, 0) 
    # g.add_edge(0, 2) 
    # g.add_edge(2, 1) 
    # g.add_edge(0, 3) 
    # g.add_edge(1, 4) 
    # g.dfs_iterative(0)
    # g.dfs(0)