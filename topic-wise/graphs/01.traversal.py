"""
Breadth-First Traversal (or Search) for a graph is similar to the Breadth-First Traversal of a tree.

The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we divide the num_vertices into two categories:

Visited and
Not visited.

How does BFS work?
Starting from the root, all the nodes at a particular level are visited first and then the nodes of the next level are traversed till all the nodes are visited.

To do this a queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue and the nodes of the current level are marked visited and popped from the queue.
"""

class UndirectedGraph:
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

class BFS:
    def __init__(self,graph:UndirectedGraph)->None:
        self.graph = graph.graph
        self.num_vertices = len(self.graph)

    def bfs(self,start_vertex:int)->None:
        """BFS for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for BFS

        >>> bfs.bfs(2)
        2 0 1 4 3 
        >>> bfs.bfs(1)
        1 0 2 3 4 
        >>> bfs.bfs(0)
        0 1 2 3 4 
        """
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.bfs_helper(start_vertex,visited)
    
    def bfs_helper(self,start_vertex:int,visited:list[bool])->None:
        """BFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start BFS from
            visited (list[bool]): list of visited nodes

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)
        """
        if start_vertex<self.num_vertices:
            queue = []
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

class DFS:
    def __init__(self,graph:UndirectedGraph)->None:
        self.graph = graph.graph
        self.num_vertices = len(self.graph)
    
    def dfs(self,start_vertex:int)->None:
        """DFS using recursive approach for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for DFS

        >>> dfs.dfs(0)
        0 1 2 4 3 
        """
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.dfs_helper(start_vertex,visited)

    def dfs_iterative(self,start_vertex:int)->None:
        """DFS using iterative approach for both connected and disconnected graphs.
        unvisited nodes are iterated to avoid missing some nodes in disconnected graphs

        Args:
            start_vertex (int): start vertex for DFS
        >>> dfs.dfs_iterative(0)
        0 2 4 3 1 
        """
        visited = [False for _ in range(self.num_vertices)]
        for vertex in range(self.num_vertices):
            if visited[vertex]==False:
                self.dfs_iterative_helper(start_vertex,visited)

    def dfs_helper(self,start_vertex:int,visited:list[bool])->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start DFS from
            visited (list[bool]): list of visited nodes

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)
        """
        if start_vertex<self.num_vertices:
            visited[start_vertex] = True
            print(start_vertex,end=" ")
            for i in range(len(self.graph[start_vertex])):
                #find neighbours of start_vertex which is not visited
                if (self.graph[start_vertex][i] == 1 and (not visited[i])):
                    self.dfs_helper(i,visited)

    def dfs_iterative_helper(self,start_vertex:int,visited:list[bool])->None:
        """DFS traversal of nodes is printed starting from source vertex

        Args:
            start_vertex (int): source vertex to start DFS from
            visited (list[bool]): list of visited nodes

            Time Complexity: O(N*N)
            Auxiliary Space: O(N)

        Limitations:
            Iterative DFS mplementation prints only vertices that are reachable from a given vertex. 
            To print all vertices of a graph, call DFS for every unvisited vertex.
        """
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


def create_graph()->UndirectedGraph:
    """ 
    Adjacency List

        0->1->2->null
        1->0->2->3->null
        2->0->1->4->null
        3->1->4->null
        4->3->2->null

    Adjacency Matrix 

        0   1   1   0   0
        1   0   1   1   0
        1   1   0   0   1
        0   1   0   0   1
        0   0   1   1   0
    
    """
    graph = UndirectedGraph(5)
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
    import doctest;doctest.testmod(extraglobs={'bfs': BFS(graph),'dfs': DFS(graph)})
