class Node:
    def __init__(self, val):
        self.parent = self
        self.value = val
        self.rank = 0
        
def find( x ):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union( x, y ):
    x = find(x)
    y = find(y)

    if y==x: return

    if x.rank > y.rank :
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G):
    n = len(G)
    K = []

    for u in range(n):
        for g in G[u]:
            v,w = g
            if u<v:
                K.append((w,u,v))
    K.sort()
    
    parent = [ Node(i) for i in range(n) ]
    ans = []

    for i in K:
        w,u,v = i
        if find(parent[u]) != find(parent[v]):
            union(parent[u],parent[v])
            ans.append(i)
    if len(ans) != n-1: return None
    return ans

#G = [ [16, 0, 1], [15, 0, 2],[ 37, 0, 3], [8, 1, 2], [22, 1, 3], [23, 2, 3]] 
G = [ [(1,16),(2,15),(3,37)], [(0,16),(2,8),(3,22)],[(0,15),(1,8),(3,23)],[(0,37),(1,22),(2,23)]]

print(Kruskal(G))