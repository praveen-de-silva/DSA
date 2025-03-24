import heapq

# class for Edges

class Edge:
    def __init__(self, weight, startVert, targetVert):
        self.weight = weight
        self.startVert = startVert
        self.targetVert = targetVert


# class for Nodes

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None # previous node that we come to this node
        self.neighbors = []
        self.minDist = float("inf")

    def __lt__(self, otherNode):
        return self.minDist < otherNode.minDist

    def addEdge(self, weight, destVert):
        edge = Edge(weight, self, destVert)
        self.neighbors.append(edge)

# --------------------
# DIJKSTRA's Algorithm
# --------------------

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, startVert):
        startVert.minDist = 0
        heapq.heappush(self.heap, startVert)

        while self.heap:
            actualVert = heapq.heappop(self.heap)

            if actualVert.visited:
                continue

            for edge in actualVert.neighbors:
                start = edge.startVert
                target = edge.targetVert
                newDist = start.minDist + edge.weight

                if newDist < target.minDist:
                    target.weight = newDist
                    target.predecessor = start
                    heapq.heappush(self.heap, target) # update the heap

            actualVert.visited = True
    
    def getShortestPath(self, vertex):
        print(f"The shortest distance to the vertex is : {vertex.minDist}")
        actualVert = vertex

        while actualVert:
            print(actualVert.name , end=" ")
            actualVert = actualVert.predecessor
            
                


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

a.addEdge(6, b)
a.addEdge(10, c)
b.addEdge(5, d)
b.addEdge(16, e)
b.addEdge(13, f)
c.addEdge(6, d)
c.addEdge(21, g)
c.addEdge(5, h)
d.addEdge(8, f)
d.addEdge(7, h)
e.addEdge(10, g)
f.addEdge(4, e)
f.addEdge(12, g)
h.addEdge(2, f)
h.addEdge(14, g)

dijkstra = Dijkstra()

dijkstra.calculate(a)
dijkstra.getShortestPath(b)