# Complete the Python function findAllPaths to find all possible paths from the source vertex to destination vertex in a directed graph.

# Function findAllPaths(vertices, gList, source, destination) takes vertices as a list of vertices, gList a dictionary that is an adjacency List representation of graph edges, source vertex, destination vertex, and returns a list of all paths from source to destination. The return value will be a List of Lists, where every path is a sequence of vertices as a List. Return an empty list if no path exists from 'source' to 'destination'.

def findAllPaths(vertices, gList, source, destination):
    def dfs(current, path, res):
        path.append(current)
        if current == destination:
            res.append(path.copy())
        else:
            for neighbor in gList.get(current, []):
                if neighbor not in path:  # avoid cycles
                    dfs(neighbor, path, res)
        path.pop()
    
    result = []
    dfs(source, [], result)
    return result

#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))