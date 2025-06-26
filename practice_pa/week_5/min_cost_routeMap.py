# A taxi driver of an online cab service provider wants to go back to his home after dropping a customer. He wants to reduce the total cost (required for fuel, toll tax, etc.) to reach home by picking some customers. He checks the routes online. So, there are some routes available from his current location to his home location where he can earn money by picking some customers.

# Write a function min_cost(route_map, source, destination) that accepts a weighted adjacency list route_map for a directed and connected graph of n vertices (labeled from 0 to n-1) in the following format:

def min_cost(route_map, source, destination):
    # Initialize distances and predecessors
    dist = {node: float('inf') for node in route_map}
    prev = {node: None for node in route_map}
    dist[source] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(len(route_map) - 1):
        for u in route_map:
            if dist[u] == float('inf'):
                continue
            for v, w in route_map[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
    
    # Check for negative cycles (optional but recommended)
    for u in route_map:
        for v, w in route_map[u]:
            if dist[u] + w < dist[v]:
                raise ValueError("Negative weight cycle detected")
    
    # Reconstruct path
    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    path.reverse()
    
    return (dist[destination], path)


size = int(input())
edges = eval(input())
s = int(input())
d = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for directed graph
    WL[ed[0]].append((ed[1],ed[2]))
print(min_cost(WL,s,d))