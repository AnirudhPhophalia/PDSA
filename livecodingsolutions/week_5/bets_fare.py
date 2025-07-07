# Write a function best_fare(flight_route, source, destination, k) that returns the minimum cost and path to travel from source to destination with at most k stops using the given weighted adjacency list flight_route, or "Not found" if no such route exists.

def addallpath(WList, u, d, visited, path, allpath):
    visited[u] = True
    path.append(u)
    if u == d:
        L = path.copy()
        allpath.append(L)
    else:
        for i in WList[u]:
            if visited[i[0]] == False:
                addallpath(WList, i[0], d, visited, path, allpath)
    path.pop()
    visited[u] = False
# Following function returns a list of all paths from s to d
# Format of returned list:- [[s,...,d],[s,...,d],...]
def findallpath(WList, s, d):
    visited = {}
    allpath = []
    for v in WList.keys():
        visited[v] = False
    path = []
    addallpath(WList, s, d, visited, path, allpath)
    return(allpath)
import heapq

def best_fare(flight_route, source, destination, k):
    # Priority queue: (total_cost, current_node, stops_used, path_list)
    heap = [(0, source, 0, [source])]
    
    while heap:
        cost, node, stops, path = heapq.heappop(heap)
        
        if node == destination:
            return (cost, path)
        
        if stops <= k:
            for nei, price in flight_route.get(node, []):
                heapq.heappush(heap, (cost + price, nei, stops + 1, path + [nei]))
    
    return "Not found"

size = int(input())
edges = eval(input())
s = int(input()) 
d = int(input())
k = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1], ed[2]))
print(best_fare(WL, s, d, k))