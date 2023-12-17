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
    - [1. Adjacency Matrix](#1-adjacency-matrix)
    - [2. Adjacency list implementation](#2-adjacency-list-implementation)
    - [BFS](#bfs)
      - [BFS Illustration](#bfs-illustration)

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

### 1. Adjacency Matrix

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
```

### 2. Adjacency list implementation

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

### BFS

Breadth-First Traversal (or Search) for a graph is similar to the Breadth-First Traversal of a tree.

The only catch here is, that, unlike trees, graphs may contain cycles, so we may come to the same node again.

To avoid processing a node more than once, we divide the vertices into two categories:

- Visited
- Not visited.

#### BFS Illustration

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
