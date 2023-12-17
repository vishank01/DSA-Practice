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

    def bfs_helper(self,start_vertex:int,visited:list)->None:
        """BFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from
            visited (list): list of visited nodes

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

    def dfs_helper(self,start_vertex:int,visited)->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from
            visited (list): list of visited nodes

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)
        """
        if start_vertex<self.num_vertices:
            visited[start_vertex] = True
            print(start_vertex,end=" ")
            for i in range(self.num_vertices):
                if (self.graph[start_vertex][i] == 1 and (not visited[i])):
                    self.dfs_helper(i,visited)

    def dfs_iterative_helper(self,start_vertex:int,visited:list)->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start DFS from
            visited (list): list of visited nodes

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)

        Limitations:
            Iterative DFS mplementation prints only vertices that are reachable from a given vertex. 
            To print all vertices of a graph, call DFS for every unvisited vertex.
        """
        print(f"\nFollowing is Depth First Traversal from source vertex {start_vertex}")
        if start_vertex<self.num_vertices:
            stack = []
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

    def bfs(self,start_vertex:int)->None:
        """BFS for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for BFS
        """
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.bfs_helper(start_vertex,visited)

    def dfs_iterative(self,start_vertex:int)->None:
        """DFS using iterative approach for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for DFS
        """
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.dfs_iterative_helper(start_vertex,visited)

    def dfs(self,start_vertex:int)->None:
        """DFS using recursive approach for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for DFS
        """
        print(f"\nPrinting DFS using Recursive Approach from source vertex {start_vertex}")
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.dfs_helper(start_vertex,visited)

def create_graph()->Graph:
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 4)
    graph.print_graph()
    return graph

if __name__=="__main__":
    graph = create_graph()

    # bfs(2) is 2 0 1 3 4
    graph.bfs(2)
    # bfs(1) is 1 0 2 3 4
    graph.bfs(1)
    # bfs(0) is 0 1 2 3 4
    graph.bfs(0)

    # dfs_iterative(0) is 0 2 4 3 1
    graph.dfs_iterative(0)
    # dfs(0) is 0 1 2 3 4 3
    graph.dfs(0)
