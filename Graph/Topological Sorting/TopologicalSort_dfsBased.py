def topological_sort(num_nodes, edges):
    # 1. Build Adjacency List
    graph = [[] for _ in range(num_nodes)]
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * num_nodes
    stack = []  # Acts as the 'ordering' array in reverse

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        
        # 2. Add to stack after all children are visited
        stack.append(node)

    # 3. Handle disconnected components
    for i in range(num_nodes):
        if not visited[i]:
            dfs(i)

    # 4. Return reversed stack
    return stack[::-1]
