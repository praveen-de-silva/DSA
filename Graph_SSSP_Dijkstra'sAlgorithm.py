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

                if newDist < target.weight:
                    target.weight = newDist
                    target.predecessor = start
                    heapq.heappush(self.push, target)

            actualVert.visited = True
    
    def getShortestPath(self, vertex):
        print(f"The shortest distance to the vertex is : {vertex.minDist}")
        actualVert = vertex

        while actualVert:
            print(actualVert.name , end=" ")
            actualVert = actualVert.predecessor
            
                


a = Node("A")
b = Node("B")

print(a<b)