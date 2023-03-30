
def DFSVisit(P,visited, G, u):
    visited[u] = True

    for v in G[u]:
        if not visited[v]:
            P[v] = u
            DFSVisit(P,visited,G,v)

def DFS(G):
    n = len(G)
    P = [None for i in range(n)]
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            DFSVisit(P,visited,G,i)
    