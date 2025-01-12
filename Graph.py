from collections import deque

class Graph:
    def __init__(self, adjList=None):
        if adjList is None:
            adjList = dict()
        self.adjList = adjList

    def __str__(self):
        return str(self.adjList)

    def addVertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            return True
        return False

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.adjList and vertex2 in self.adjList:
            if vertex2 not in self.adjList[vertex1]:
                self.adjList[vertex1].append(vertex2)
                self.adjList[vertex2].append(vertex1)
                return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adjList and vertex2 in self.adjList:
            try:
                self.adjList[vertex1].remove(vertex2)
                self.adjList[vertex2].remove(vertex1)
            except ValueError:
                return False
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self.adjList:
            for vert in self.adjList[vertex]:
                self.adjList[vert].remove(vertex)
            del self.adjList[vertex]
            return True 
        return False

    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])

        while queue:
            crntVert = queue.popleft() # this line has O(1)
            print(crntVert, queue, visited)

            for adjVert in self.adjList[crntVert]:
                if adjVert not in visited:
                    visited.add(adjVert)
                    queue.append(adjVert)
                



# BFS my method :
# def bfs(graph, vertex, indexSeen = 0, seen=[]):
#     print(vertex, indexSeen, seen)
    
#     if vertex not in seen:
#         seen.append(vertex)
        
    
#     for otherVert in graph.adjList[vertex]:
#         if otherVert not in seen:
#             seen.append(otherVert)

#     if indexSeen+1<len(seen):
#         return bfs(graph, seen[indexSeen+1], indexSeen+1 ,seen)
#     return 

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            crntVert = stack.pop()

            if crntVert not in visited:
                print(crntVert)
                visited.add(crntVert)

            for adjVert in self.adjList[crntVert]:
                if adjVert not in visited:
                    stack.append(adjVert)
    




grp = Graph()
grp.addVertex('A')
grp.addVertex('B')
grp.addVertex('C')
grp.addVertex('D')
grp.addVertex('E')
grp.addVertex('F')
grp.addVertex('G')

grp.addEdge('A','B')
grp.addEdge('A','C')
grp.addEdge('B','D')
grp.addEdge('B','G')
grp.addEdge('C','D')
grp.addEdge('C','E')
grp.addEdge('D','F')
grp.addEdge('E','F')
grp.addEdge('F','G')

print(grp)
#bfs(grp, 'A')
grp.dfs('A')


