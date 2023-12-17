"""
To find cycle in a directed graph we can use the Depth First Traversal (DFS) technique. 
It is based on the idea that there is a cycle in a graph only if there is a back edge 
[i.e., a node points to one of its ancestors] present in the graph.

Directed Graph Cycle Detection

To detect a back edge, we need to keep track of the nodes visited till now and the nodes that are in the current recursion stack 
[i.e., the current path that we are visiting]. If during recursion, we reach a node that is already in the recursion stack, 
there is a cycle present in the graph.

UnDirected Graph Detection

To find the back edge to any of its ancestors keep a visited array and if there is a back edge to any visited node then there is a loop and return true.
A back edge is an edge that is indirectly joining a node to itself (self-loop) or one of its ancestors in the tree produced by DFS. 

Difference between Directed and UnDirected detection is 

    -- In Directed even if current node is visited, we need to check if it is present in recursion stack 
        as every path has direction
    -- In Undirected graph if current node is visited, then just check if parent is not same (always this is cycle so avoid this)
        then return True

"""

class UnDirectedGraph:
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
        print("\n")

class DirectedGraph:
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

    def remove_edge(self,v1:int,v2:int)->None:
        if v1<self.num_vertices and v2<self.num_vertices:
            self.graph[v1][v2]=0

    def remove_all_edges(self)->None:
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                self.graph[i][j]=0
    
    def print_graph(self):
        for row in self.graph:
            for val in row:
                print('{:4}'.format(val),end="")
            print("\n")
        print("\n")

class DirectedGraphCycleDetector:
    def __init__(self,graphs:list[DirectedGraph])->None:
        self.graphs = graphs
    
    def detect_cycle_in_graphs(self)->list[bool]:
        """ Fuction to Detect Cycles in Graph using DFS
        Returns:
            list[bool] : list of results for given input graphs

        >>> directed_graph.detect_cycle_in_graphs()
        [True]
        """
        results = []
        for graph in self.graphs:
            result = False
            num_vertices = len(graph.graph)
            visited = [False for _ in range(num_vertices)]
            recursion_stack = [False for _ in range(num_vertices)]
            for vertex in range(num_vertices):
                if visited[vertex]==False:
                    if self.detect_cycle_in_graph_helper(graph.graph,num_vertices,vertex,visited,recursion_stack):
                        result = True
            results.append(result)
        return results

    def detect_cycle_in_graph_helper(self,graph:DirectedGraph,num_vertices:int,start_vertex:int,visited:list[bool],recursion_stack:list[bool])->bool:
        """ Helper function to Detect Cycles in Graph using DFS

        Args:
            start_vertex (int): source vertex to start DFS from
            visited (list[bool]): list of visited nodes
            recursion_stack (list[bool]): list of nodes in current recursion stack

        Returns:
            bool : True/False 
        """
        if start_vertex<num_vertices:
            #Mark current node as visited and add to recursion_stack
            visited[start_vertex] = True
            recursion_stack[start_vertex]=True
            for i in range(num_vertices):
                #check if i is neighbour for start_vertex
                if graph[start_vertex][i]==1:
                    if visited[i]==False:
                        if self.detect_cycle_in_graph_helper(graph,num_vertices,i,visited,recursion_stack):
                            return True
                    #if any neighbour is visited and is in recursion_stack then graph is cyclic
                    elif recursion_stack[i]:
                        return True
            # The node needs to be popped from recursion_stack before function ends
            recursion_stack[start_vertex]=False

class UnDirectedGraphCycleDetector:
    def __init__(self,graphs:list[UnDirectedGraph])->None:
        self.graphs = graphs
    
    def detect_cycle_in_graphs(self)->bool:
        """ Fuction to Detect Cycles in Graph using DFS
        Returns:
            bool : True/False

        >>> undirected_graph.detect_cycle_in_graphs()
        [True,False]
        """
        results = []
        for graph in self.graphs:
            result = False
            num_vertices = len(graph.graph)
            visited = [False for _ in range(num_vertices)]
            recursion_stack = [False for _ in range(num_vertices)]
            for vertex in range(num_vertices):
                if visited[vertex]==False:
                    if self.detect_cycle_in_graph_helper(graph.graph,num_vertices,vertex,visited,recursion_stack):
                        result = True
            results.append(result)
        return results

    def detect_cycle_in_graph_helper(self,graph:UnDirectedGraph,num_vertices:int,start_vertex:int,visited:list[bool],parent:int)->bool:
        """ Helper function to Detect Cycles in Graph using DFS

        Args:
            start_vertex (int): source vertex to start DFS from
            visited (list[bool]): list of visited nodes
            parent (int): parent vertex node id

        Returns:
            bool : True/False 
        """
        if start_vertex<num_vertices:
            #Mark current node as visiteds
            visited[start_vertex] = True
            for i in range(num_vertices):
                #check if i is neighbour for start_vertex
                if graph[start_vertex][i]==1:
                    if visited[i]==False:
                        if self.detect_cycle_in_graph_helper(graph,num_vertices,i,visited,start_vertex):
                            return True
                    #if any neighbour is visited and is in recursion_stack then graph is cyclic
                    elif parent!=i:
                        return True

def create_directed_graphs()->list[DirectedGraph]:
    """ 
    Adjacency List

        0->0->1->2->null
        1->>2->null
        2->3->null

    Adjacency Matrix 

        1   1   1   0
        0   0   1   0
        0   0   0   1
        0   0   0   0
    
    """
    g1 = DirectedGraph(4)
    g1.add_edge(0,0)
    g1.add_edge(0,1)
    g1.add_edge(0,2)
    g1.add_edge(1,2)
    g1.add_edge(2,3)
    g1.print_graph()
    return [g1]

def create_undirected_graphs()->list[UnDirectedGraph]:
    """ 
    Adjacency List

        0->0->1->2->null
        1->>2->null
        2->3->null

        0->1->null
        1->2->null

    Adjacency Matrix 

        1   1   1   0
        1   0   1   0
        1   1   0   1
        0   0   1   0

        0   1   0
        1   0   1
        0   1   0
    
    """
    g1 = UnDirectedGraph(4)
    # graph.add_edge(0,0)
    g1.add_edge(0,1)
    g1.add_edge(0,2)
    g1.add_edge(1,2)
    g1.add_edge(2,3)
    g1.print_graph()

    g2 = UnDirectedGraph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    
    return [g1,g2]

if __name__=="__main__":
    # import doctest;doctest.testmod(extraglobs={'directed_graph': DirectedGraphCycleDetector(create_directed_graphs())})
    print(DirectedGraphCycleDetector(create_directed_graphs()).detect_cycle_in_graphs())
    print(UnDirectedGraphCycleDetector(create_undirected_graphs()).detect_cycle_in_graphs())