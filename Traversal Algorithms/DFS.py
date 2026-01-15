from collections import deque

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        print(self.graph)

        for i in range(self.size):
            print(f"{i} -> ", end='')
            for v in self.graph[i]:
                print(f"{v}  ", end='')
            print()

    def DFS(self, start):
        q = deque()
        q.append(start)
        visited = ["w" for _ in range(self.size)]
        visited[start] = "b"

        while q:
            crntNode = q.pop()
            # exploring crnt node
            print(crntNode)

            # visiting neighbors
            for adjNode in self.graph[crntNode]:
                if visited[adjNode] == "w":
                    q.appendleft(adjNode)
                    visited[adjNode] = "b"
                print(visited)


if __name__=='__main__':
    print("Hello")

    gp = Graph(7)

    gp.addEdge(0, 1)
    gp.addEdge(0, 2)
    gp.addEdge(1, 3)
    gp.addEdge(1, 4)
    gp.addEdge(2, 5)
    gp.addEdge(2, 6) 

    gp.printGraph()

    print("----------------------\nBFS:")
    gp.DFS(0)
