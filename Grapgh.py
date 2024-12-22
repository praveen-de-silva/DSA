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

grp = Graph()
print(grp.addEdge('a','b'))
print(grp.addEdge('b','a'))

print(grp)