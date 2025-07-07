# A country's defense organization wants to set up a private fiber network to connect all its camps around the country which will be disconnected from the INTERNET (world wide web). It wants to exclude only one camp, which will be connected to the INTERNET. Camps that can be connected to each other via fiber and the associated cable cost to connect them is given as an adjacency list representation Alist for all n camp of the company in the format below.

import heapq

def connectCamps(Alist, exCamp):
    # Remove exCamp from graph and all its edges
    graph = {}
    for u in Alist:
        if u == exCamp:
            continue
        graph[u] = []
        for v, cost in Alist[u]:
            if v != exCamp:
                graph[u].append((cost, v))

    if not graph:
        return -1

    visited = set()
    start = next(iter(graph))  # start from any remaining camp
    min_heap = [(0, start)]  # (cost, camp)
    total_cost = 0

    while min_heap and len(visited) < len(graph):
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        for edge_cost, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_cost, v))

    return total_cost if len(visited) == len(graph) else -1
