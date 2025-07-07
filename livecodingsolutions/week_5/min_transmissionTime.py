# You are given a network of n nodes, labelled from 0 to n-1. You are also given travel_times, a list of signal travel times in as directed edges travel_times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# Write a function min_transmission_time(n, travel_times, s) that accept number of nodes n, a list travel_times and a source node s to send the signal . The function returns the minimum time required for the signal sent by the source node s to be received by all the remaining n-1 nodes. If it is impossible to obtain a signal for all n-1 nodes, return -1.

import heapq

def min_transmission_time(n, travel_times, s):
    from collections import defaultdict

    # Step 1: Build graph
    graph = defaultdict(list)
    for u, v, w in travel_times:
        graph[u].append((v, w))  # directed edge from u to v

    # Step 2: Dijkstra's algorithm
    min_time = [float('inf')] * n
    min_time[s] = 0
    visited = set()
    heap = [(0, s)]  # (time, node)

    while heap:
        time, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            if min_time[v] > time + w:
                min_time[v] = time + w
                heapq.heappush(heap, (min_time[v], v))

    # Step 3: Result
    if len([t for t in min_time if t != float('inf')]) < n:
        return -1
    return max(min_time)

n = int(input())
edges = eval(input())
s = int(input())
print(min_transmission_time(n, edges, s))