from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self,vertices:int)->None:
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self,u:int,v:int):
        self.graph[u].append(v)

    def topological_sort_dfs(self):
        """prints topologically sorted vertices using DFS
        Approach is to put vertex to stack if all of it's children are visited (this is slight modification of DFS)
        in this way all the children aren't printed first before it's corresponding parent is printed(ensuring u is before v)
        """
        stack = []
        visited = [False for _ in range(self.vertices)]

        def helper(vertex:int,visited:list[bool],stack:list[int]):
            visited[vertex]=True
            for adjacent_node in self.graph[vertex]:
                if visited[adjacent_node]==False:
                    return helper(adjacent_node,visited,stack)
            stack.append(vertex)

        for i in range(self.vertices):
            if visited[i]==False:
                helper(i,visited,stack)
        # while len(stack)>0:
        #     print(stack.pop())
        return print(stack[::-1])

    def topological_sort_bfs(self):
        queue = deque()
        in_degrees = [0 for _ in range(self.vertices)]

        for node in self.graph:
            for adjacent_node in self.graph[node]:
                in_degrees[adjacent_node]+=1

        for i in range(self.vertices):
            if in_degrees[i]==0:
                queue.append(i)

        output = []
        vertices_cnt=0 

        while len(queue)>0:
            source_node = queue.popleft()
            #output can also be printed but it is stored here just to avoid printing data for cyclic graph
            output.append(source_node)
            for adjacent_node in self.graph[source_node]:
                in_degrees[adjacent_node]-=1
                if in_degrees[adjacent_node]==0:
                    queue.append(adjacent_node)
            vertices_cnt+=1
        if vertices_cnt!=self.vertices:
            print("Cycles are present in the graph hence cannot be sorted!")
        else:
            print(output)

if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    # g.add_edge(2, 5)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological sort using DFS")
    #[5, 4, 2, 3, 1, 0]
    g.topological_sort_dfs()

    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print("Topological sort using BFS")
    #[4, 5, 2, 0, 3, 1]
    g.topological_sort_bfs()
