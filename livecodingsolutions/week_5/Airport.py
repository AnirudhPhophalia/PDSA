# An Airline company wants to make an airport to connect n cities labeled 0 to n-1 all across the country.
# Write a function Airport(distance_map) that accepts a weighted adjacency list distance_map in the following format:

import heapq

def Airport(distance_map):
    n = len(distance_map)
    visited = set()
    total_cost = 0

    # Start from any node (say, 0)
    start_node = next(iter(distance_map))
    min_heap = [(0, start_node)]  # (cost, node)

    while min_heap and len(visited) < n:
        cost, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += cost
        for v, edge_cost in distance_map[u]:
            if v not in visited:
                heapq.heappush(min_heap, (edge_cost, v))

    return total_cost if len(visited) == n else -1

size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(Airport(WL))