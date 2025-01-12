class Graph:
    def __init__(self, gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict

    def bfs(self, start, end):
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node == end:
                return path

            for adj in self.gDict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)
            print(queue)


custDic = {
    'A' : ['B', 'C'],
    'B' : ['D', 'G'],
    'C' : ['D', 'E'],
    'D' : ['F'],
    'E' : ['F'],
    'G' : ['F']
}

g = Graph(custDic)
print(g.bfs('A', 'F'))
