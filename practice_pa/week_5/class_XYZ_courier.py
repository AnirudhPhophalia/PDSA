# A courier company XYZ provides courier service between n cities labeled 0 to n-1, where customers can send items from any city to any other city. The company follows the shortest path to deliver items and charges 5 Rs. per kilometer distance. The company wants to develop an inquiry system where customers can get the information on the cost and route for their courier.

# Write a class XYZ_Courier that accepts a weighted adjacency list Route_map for an undirected and connected graph at the time of object creation in following format:

import heapq

class XYZ_Courier:
    def __init__(self, Route_map):
        self.Route_map = Route_map

    def dijkstra(self, source):
        dist = {node: float('inf') for node in self.Route_map}
        parent = {node: None for node in self.Route_map}
        dist[source] = 0
        heap = [(0, source)]

        while heap:
            curr_dist, u = heapq.heappop(heap)
            if curr_dist > dist[u]:
                continue
            for v, weight in self.Route_map[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(heap, (dist[v], v))
        return dist, parent

    def cost(self, source, destination):
        dist, _ = self.dijkstra(source)
        return dist[destination] * 5

    def route(self, source, destination):
        _, parent = self.dijkstra(source)
        path = []
        curr = destination
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        return path[::-1]

size = int(input())
edges = eval(input())
s=int(input())
d=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))