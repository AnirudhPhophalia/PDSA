class MakeUnionFind:
    def __init__(self):
        self.components = {}
        self.members = {}
        self.size = {}

    def make_union_find(self, vertices):
        for vertex in range(vertices):
            self.components[vertex] = vertex
            self.members[vertex] = [vertex]
            self.size[vertex] = 1
    
    def find(self, vertex):
        return self.components[vertex]

    def union(self, u, v):
        c_old = self.components[u]
        c_new = self.components[v]

        # Always add member in components which have greater size
        if self.size[c_new] >= self.size[c_old]:
            for x in self.members[c_old]:
                self.components[x] = c_new
                self.members[c_new].append(x)
            self.size[c_new] += 1
        else:
            for x in self.members[c_new]:
                self.components[x] = c_old
                self.members[c_old].append(x)
            self.size[c_old] += 1

def findRedundantEdges(E, n):
    st = MakeUnionFind()
    st.make_union_find(n)
    redlist = []
    for edge in E:
        if st.find(edge[0]) == st.find(edge[1]):
            redlist.append(edge)
        else:
            st.union(edge[0], edge[1])
    return redlist

n = int(input())
E=eval(input())
print(findRedundantEdges(E,n))