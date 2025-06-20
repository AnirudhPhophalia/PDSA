# Given an undirected graph G, write a Python function to compute the number of connected components. A set of nodes form a connected component in an undirected graph if there exists a path between every pair of nodes in this set.

# Write a Python function findComponents_undirectedGraph(vertices, edges), that accepts a list of vertices and a list of tuples that represent edges, and returns the number of connected components in the graph formed by vertices and edges. Each tuple (i, j) in edges represents an edge between vertices i and j.

# For a completely connected graph there is only one connected component, hence the function should return 1.

def findComponents_undirectedGraph(vertices, edges):
    from collections import defaultdict, deque

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    def bfs(start):
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for vertex in vertices:
        if vertex not in visited:
            bfs(vertex)
            components += 1

    return components
