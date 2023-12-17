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

    g = AdjacencyMatrix(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.print_graph()
