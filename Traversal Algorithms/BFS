from collections import deque

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def printGraph(self):
        print(self.graph)

        for i in range(self.size):
            print(f"{i} -> ", end='')
            for v in self.graph[i]:
                print(f"{v[0]}({v[1]})  ", end='')
            print()

    def BFS(self, start):
        nodesQueue = deque()
        visited = ["w" for _ in range(self.size)]

        nodesQueue.append(start)

        while nodesQueue:
            crntNode = nodesQueue.popleft()
            
            # if already visited, continue to the next
            if visited[crntNode] == "b":
                continue

            # visiting crnt node
            print(crntNode)
            visited[crntNode] = "b"

            # visiting neighbors
            for adjNode, w in self.graph[crntNode]:
                if visited[adjNode] == "w":
                    nodesQueue.append(adjNode)
                    visited[adjNode] = "g"
                print(visited)






if __name__=='__main__':
    print("Hello")

    gp = Graph(7)

    gp.addEdge(0, 1, 10)
    gp.addEdge(0, 2, 30)
    gp.addEdge(1, 3, 15)
    gp.addEdge(1, 4, 20)
    gp.addEdge(2, 5, 40)
    gp.addEdge(2, 6, 25) 

    gp.printGraph()

    print("----------------------\nBFS:")
    gp.BFS(0)
