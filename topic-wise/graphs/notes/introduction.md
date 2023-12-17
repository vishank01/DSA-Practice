# Table of Contents

- [Table of Contents](#table-of-contents)
  - [Graphs Theory](#graphs-theory)
  - [Types Of Graph](#types-of-graph)
    - [1. Null Graph](#1-null-graph)
    - [2. Trivial Graph](#2-trivial-graph)
    - [3. Undirected Graph](#3-undirected-graph)
    - [4. Directed Graph](#4-directed-graph)
    - [5. Connected Graph](#5-connected-graph)
    - [6. Disconnected Graph](#6-disconnected-graph)
    - [7. Regular Graph](#7-regular-graph)
    - [8. Complete Graph](#8-complete-graph)
    - [9. Cycle Graph](#9-cycle-graph)
    - [10. Cyclic Graph](#10-cyclic-graph)
    - [11. Directed Acyclic Graph](#11-directed-acyclic-graph)
    - [12. Bipartite Graph](#12-bipartite-graph)
    - [13. Weighted Graph](#13-weighted-graph)
  - [Representation of Graphs](#representation-of-graphs)
    - [1. Adjacency Matrix Implementation](#1-adjacency-matrix-implementation)
    - [2. Adjacency List Implementation](#2-adjacency-list-implementation)
  - [Breadth First Traversal](#breadth-first-traversal)
    - [BFS Illustration](#bfs-illustration)
  - [Depth First Traversal](#depth-first-traversal)
    - [DFS Illustration](#dfs-illustration)
  - [BFS for Disconnected Graph](#bfs-for-disconnected-graph)
  - [Traversals DFS and BFS implementation](#traversals-dfs-and-bfs-implementation)
  - [Applications,Advantages and Disadvantages of BFS](#applicationsadvantages-and-disadvantages-of-bfs)
    - [Applications of BFS](#applications-of-bfs)
    - [Advantages of BFS](#advantages-of-bfs)
    - [Disadvantages of BFS](#disadvantages-of-bfs)
  - [Applications,Advantages and Disadvantages of DFS](#applicationsadvantages-and-disadvantages-of-dfs)
    - [Applications of DFS](#applications-of-dfs)
    - [Advantages of DFS](#advantages-of-dfs)
    - [Disadvantages of DFS](#disadvantages-of-dfs)

## Graphs Theory

Graphs are non-linear data startuctures. vertexes and edges are main components of the graphs.

A graph with N vertexes can have N-1 number of graphs.

![Introduction to graphs](https://media.geeksforgeeks.org/wp-content/uploads/20200630111809/graph18.jpg)

## Types Of Graph

### 1. Null Graph

A graph is known as a null graph if there are no edges in the graph.

### 2. Trivial Graph

Graph having only a single vertex, it is also the smallest graph possible.

![Null and Trivial Graphs](https://media.geeksforgeeks.org/wp-content/uploads/20200630113942/null_graph_trivial.jpg)

### 3. Undirected Graph

A graph in which edges do not have any direction. That is the nodes are unordered pairs in the definition of every edge.

### 4. Directed Graph

A graph in which edge has direction. That is the nodes are ordered pairs in the definition of every edge.
![Alt text](image-1.png)

### 5. Connected Graph

The graph in which from one node we can visit any other node in the graph is known as a connected graph.

### 6. Disconnected Graph

The graph in which at least one node is not reachable from a node is known as a disconnected graph.

![Conncted and Disconnected Graph](https://media.geeksforgeeks.org/wp-content/uploads/20200630121400/connected1.jpg)

### 7. Regular Graph

The graph in which the degree of every vertex is equal to K is called K regular graph.

### 8. Complete Graph

The graph in which from each node there is an edge to each other node.
![Regular and Complete Graphs](https://media.geeksforgeeks.org/wp-content/uploads/20200630122008/regular.jpg)
.

### 9. Cycle Graph

The graph in which the graph is a cycle in itself, the degree of each vertex is 2.

### 10. Cyclic Graph

A graph containing at least one cycle is known as a Cyclic graph.
![Cycle and Cyclic Graph](https://media.geeksforgeeks.org/wp-content/uploads/20200630122225/cyclic.jpg)

### 11. Directed Acyclic Graph

A Directed Graph that does not contain any cycle.

### 12. Bipartite Graph

A graph in which vertex can be divided into two sets such that vertex in each set does not contain any edge between them.

![Directed Acyclic and Bipartite Graph](https://media.geeksforgeeks.org/wp-content/uploads/20200630122552/bipartite1.jpg)

### 13. Weighted Graph

 A graph in which the edges are already specified with suitable weight is known as a weighted graph.
 Weighted graphs can be further classified as directed weighted graphs and undirected weighted graphs.

## Representation of Graphs

There are two ways to store a graph:

1. Adjacency Matrix

    ![Adjacency Matrix](https://media.geeksforgeeks.org/wp-content/uploads/20200630124726/adjacency_mat1.jpg)
2. Adjacency List

   ![Adjacency List](https://media.geeksforgeeks.org/wp-content/uploads/20200630125356/adjacency_list.jpg)

| Action        | Adjacency Matrix | Adjacency List |
|:--------------|:----------------:|:--------------:|
| Adding Edge   |       O(1)       |      O(1)      |
| Removing Edge |       O(1)       |      O(N)      |
| Initializing  |      O(N*N)      |      O(N)      |

### 1. Adjacency Matrix Implementation

```python
class AdjacencyMatrix:
    def __init__(self,num_vertices:int) -> None:
        """Implementation of Graphs in Adjacency matrix 
            Time Complexity:
                Addition of node is O(1)
                Removal of node is O(1)
                Initialization is O(N*N)

        Args:
            num_vertices (int): number of num_vertices for a graph
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
    
    def print_graph(self):
        for row in self.graph:
            for val in row:
                print('{:4}'.format(val),end="")
            print("\n")

if __name__=="__main__":
    g = AdjacencyMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_graph()
    g.remove_edge(0,2)
    g.remove_edge(3,2)
    print("\n**\n")
    g.print_graph()
```

### 2. Adjacency List Implementation

```python
class AdjacencyList:
    def __init__(self,num_vertices:int) -> None:
        """Implementation of Graphs in Adjacency list 
            Time Complexity:
                Addition of node is O(1)
                Removal of node is O(N)
                Initialization is O(N)

        Args:
            num_vertices (int): number of num_vertices for a graph
        """
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(self.num_vertices)]

    def add_edge(self,v1:int,v2:int):
        if v1<self.num_vertices and v2<self.num_vertices:
            self.graph[v1].append(str(v2))
            self.graph[v2].append(str(v1))

    def remove_edge(self,v1:int,v2:int):
        if v1<self.num_vertices and v2<self.num_vertices:
            self.graph[v1].remove(str(v2))
            self.graph[v2].remove(str(v1))

    def print_graph(self):
        for _id,vertex in enumerate(self.graph):
            print(f"{_id}->{'->'.join(vertex+['null'])}")

if __name__=="__main__":
    g = AdjacencyList(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_graph()
    g.remove_edge(0,2)
    g.remove_edge(3,2)
    print("\n**\n")
    g.print_graph()
```

## Breadth First Traversal

Breadth-First Traversal (or Search) for a graph is similar to the Breadth-First Traversal of a tree.

The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again.

To avoid processing a node more than once, we divide the vertices into two categories:

- Visited
- Not visited.

### BFS Illustration

- Starting from the root, all the nodes at a particular level are visited first and then the nodes of the next level are traversed till all the nodes are visited.

- To do this a queue is used. All the adjacent unvisited nodes of the current level are pushed into the queue and the nodes of the current level are marked visited and popped from the queue.

Let us understand the working of the algorithm with the help of the following example.

**Step1:** Initially queue and visited arrays are empty.

![Step 1](https://media.geeksforgeeks.org/wp-content/uploads/20221221015614/1-768.png)

**Step2:** Push node 0 into queue and mark it visited.

![Step 2](https://media.geeksforgeeks.org/wp-content/uploads/20221221015623/2-768.png)

**Step 3:** Remove node 0 from the front of queue and visit the unvisited neighbours and push them into queue.

![Step 3](https://media.geeksforgeeks.org/wp-content/uploads/20221221015630/3-768.png)

**Step 4:** Remove node 1 from the front of queue and visit the unvisited neighbours and push them into queue.

![Step 4](https://media.geeksforgeeks.org/wp-content/uploads/20221221015739/4-768.png)

**Step 5:** Remove node 2 from the front of queue and visit the unvisited neighbours and push them into queue.

![Step 5](https://media.geeksforgeeks.org/wp-content/uploads/20221221015757/5-768.png)

**Step 6:** Remove node 3 from the front of queue and visit the unvisited neighbours and push them into queue.

As we can see that every neighbours of node 3 is visited, so move to the next node that are in the front of the queue.

![Step 6](https://media.geeksforgeeks.org/wp-content/uploads/20221221015827/6-768.png)

**Steps 7:** Remove node 4 from the front of queue and visit the unvisited neighbours and push them into queue.

As we can see that every neighbours of node 4 are visited, so move to the next node that is in the front of the queue.

![Step 7](https://media.geeksforgeeks.org/wp-content/uploads/20221221015827/6-768.png)

## Depth First Traversal

Depth First Traversal (or DFS) for a graph is similar to Depth First Traversal of a tree.

The only catch here is, that, unlike trees, graphs may contain cycles (a node may be visited twice).

To avoid processing a node more than once, use a boolean visited array.

**_A graph can have more than one DFS traversal._**

### DFS Illustration

Depth-first search is an algorithm for traversing or searching tree or graph data structures.

The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

**Step1:** Initially stack and visited arrays are empty.

![Step 1](https://media.geeksforgeeks.org/wp-content/uploads/20230510170648/DFS-(1)-copy.webp)

**Step 2:** Visit 0 and put its adjacent nodes which are not visited yet into the stack.

![Step 2](https://media.geeksforgeeks.org/wp-content/uploads/20230510170831/DFS-(2)-copy.webp)

**Step 3:** Now, Node 1 at the top of the stack, so visit node 1 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.

![Step 3](https://media.geeksforgeeks.org/wp-content/uploads/20230510171121/DFS-(3)-copy.webp)

**Step 4:** Now, Node 2 at the top of the stack, so visit node 2 and pop it from the stack and put all of its adjacent nodes which are not visited (i.e, 3, 4) in the stack.

![Step 4](https://media.geeksforgeeks.org/wp-content/uploads/20230510171029/DFS-(4)-copy.webp)

**Step 5:** Now, Node 4 at the top of the stack, so visit node 4 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.

![Step 5](https://media.geeksforgeeks.org/wp-content/uploads/20230510171653/DFS-(5)-copy.webp)

**Step 6:** Now, Node 3 at the top of the stack, so visit node 3 and pop it from the stack and put all of its adjacent nodes which are not visited in the stack.

![Step 6](https://media.geeksforgeeks.org/wp-content/uploads/20230510171604/DFS-(6)-copy.webp)

_Now, Stack becomes empty, which means we have visited all the nodes and our DFS traversal ends._


## BFS for Disconnected Graph

Traversing a disconnected graph in BFS differs from traversing a connected graph. The main difference is that not all the vertices of a disconnected graph can be visited using all other vertices. 

`So after implementing BFS, you have to check whether or not all the vertices are visited`. If some vertices remain, you must implement BFS again with that vertex. 

**Example:**

 Output: `0 1 2 3 4 5 6`

![BFS for Disconnected Graph](https://files.codingninjas.in/article_images/bfs-in-disconnected-graph-1-1661429482.webp)

Explanation:

When we start with vertex 0, vertices 1 and 2 are added to the queue, and via vertex 1, vertex 3 is added. Since the graph is disconnected, vertex 4, 5, and 6 can not be visited by any visited vertex. 
So we have to start the BFS again with vertex 4; now, vertices 5 and 6 are visited. 

## Traversals DFS and BFS implementation

```python
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
```

## Applications,Advantages and Disadvantages of BFS

### Applications of BFS

1. `Shortest Path and Minimum Spanning Tree for unweighted graph`: In an unweighted graph, the shortest path is the path with the least number of edges.

   With Breadth First, we always reach a vertex from a given source using the minimum number of edges. Also, in the case of unweighted graphs, any spanning tree is Minimum Spanning Tree and we can use either DFS or BFS for finding a spanning tree.

2. `Minimum Spanning Tree for weighted graphs`: We can also find Minimum Spanning Tree for weighted graphs using BFT, but the condition is that `the weight should be non-negative` and the same for each pair of vertices.

3. `Peer-to-Peer Networks`: In Peer-to-Peer Networks like BitTorrent, Breadth First Search is used to find all neighbor nodes.

4. `Crawlers in Search Engines`: Crawlers build an index using Breadth First. The idea is to start from the source page and follow all links from the source and keep doing the same. DFS can also be used for crawlers, but the `advantage of BFS is, the depth or levels of the built tree can be limite`d.

5. `Social Networking Websites`: In social networks, we can find people within a given distance ‘k’ from a person using Breadth First Search till ‘k’ levels.

6. `GPS Navigation systems`: Breadth First Search is used to find all neighboring locations.

7. `Broadcasting in Network`: In networks, a broadcasted packet follows Breadth First Search to reach all nodes.

8. `In Garbage Collection`: Breadth First Search is used in copying garbage collection using Cheney’s algorithm. Breadth First Search is preferred over Depth First Search because of a better locality of reference.

9. `Cycle detection in undirected graph`: In undirected graphs, either BFS or DFS can be used to detect a cycle. Also, We can use BFS to detect cycle in a directed graph.

10. `Ford–Fulkerson algorithm`: In Ford–Fulkerson algorithm, we can either use BFS or DFS to find the maximum flow. `BFS is preferred as it reduces the worst-case time complexity to O(VE2)`.

11. `To test if a graph is Bipartite`: We can either use BFS or DFS.

12. `Path Finding`: We can either use BFS or DFS to find if there is a path between two vertices.

13. `Finding all nodes within one connected component`: We can either use BFS or DFS to find all nodes reachable from a given node.

14. `AI`: In AI, BFS is used in traversing a game tree to find the best move.

15. `Network Security`: In the field of network security, BFS is used in traversing a network to find all the devices connected to it.

16. `Connected Component`: We can find all connected components in an undirected graph.

17. `Topological sorting`: BFS can be used to find a topological ordering of the nodes in a directed acyclic graph (DAG).

18. `Image processing`: BFS can be used to flood-fill an image with a particular color or to find connected components of pixels.

19. `Recommender systems`: BFS can be used to find similar items in a large dataset by traversing the items’ connections in a similarity graph.

20. `Other usages`: Many algorithms like `Prim’s Minimum Spanning Tree` and `Dijkstra’s Single Source Shortest Path` use structures similar to Breadth First Search.

### Advantages of BFS

- BFS will `never get trapped` exploring the useful path forever.
- If there is a solution, BFS will definitely find it.
- If there is more than one solution then BFS can find the minimal one that requires less number of steps.
- Low storage requirement – linear with depth.
Easily programmable.

### Disadvantages of BFS

The main drawback of BFS is its `memory requirement`. Since each level of the graph must be saved in order to generate the next level and the amount of memory is proportional to the number of nodes stored the `space complexity of BFS is O(bd)`, where b is the branching factor(the number of children at each node, the outdegree) and d is the depth.

As a result, `BFS is severely space-bound in practice` so will exhaust the memory available on typical computers in a matter of minutes.

## Applications,Advantages and Disadvantages of DFS

### Applications of DFS

1. `Detecting cycle in a graph`: A graph has a cycle if and only if we see a back edge during DFS. So we can run DFS for the graph and check for back edges.

2. `Path Finding`: We can specialize the DFS algorithm to find a path between two given vertices u and z.

    Call DFS(G, u) with u as the start vertex.
    Use a stack S to keep track of the path between the start vertex and the current vertex.
    As soon as destination vertex z is encountered, return the path as the contents of the stack

3. `Topological Sorting`: Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs.

   In computer science, applications of this type arise in instruction scheduling, ordering of formula cell evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of compilation tasks to perform in makefiles, data serialization, and resolving symbol dependencies in linkers.

4. `To test if a graph is bipartite`: We can augment either BFS or DFS when we first discover a new vertex, color it opposite its parents, and for each other edge, check it doesn’t link two vertices of the same color. The first vertex in any connected component can be red or black.

5. `Finding Strongly Connected Components of a graph`: A directed graph is called strongly connected if there is a path from each vertex in the graph to every other vertex. (See this for DFS-based algo for finding Strongly Connected Components)

6. `Solving puzzles with only one solution`: such as mazes. (DFS can be adapted to find all solutions to a maze by only including nodes on the current path in the visited set.).

7. `Web crawlers`: Depth-first search can be used in the implementation of web crawlers to explore the links on a website.

8. `Maze generation`: Depth-first search can be used to generate random mazes.

9. `Model checking`: Depth-first search can be used in model checking, which is the process of checking that a model of a system meets a certain set of properties.

10. `Backtracking`: Depth-first search can be used in backtracking algorithms.

### Advantages of DFS

- `Memory requirement is only linear` with respect to the search graph. This is in contrast with breadth-first search which requires more space. The reason is that the algorithm only needs to store a stack of nodes on the path from the root to the current node.
- The time complexity of a depth-first Search to depth d and branching factor b (the number of children at each node, the outdegree) is `O(bd)` since it generates the same set of nodes as breadth-first search, but simply in a different order. Thus practically depth-first search is time-limited rather than space-limited.
  
- If depth-first search finds solution without exploring much in a path then the time and space it takes will be very less.

- `DFS requires less memory` since only the nodes on the current path are stored. By chance DFS may find a solution without examining much of the search space at all.

### Disadvantages of DFS

- The disadvantage of DFS is that there is a possibility that it may down the left-most path forever. `Even a finite graph can generate an infinite tree.`
  
    One solution to this problem is to impose a cutoff depth on the search. Although ideal cutoff is the solution depth d and this value is rarely known in advance of actually solving the problem.

- If the chosen cutoff depth is less than d, the algorithm will fail to find a solution, whereas if the cutoff depth is greater than d, a large price is paid in execution time, and the first solution found may not be an optimal one.

- `DFS is not guaranteed to find the solution`.
 And there is no guarantee to find a minimal solution, if more than one solution.
 