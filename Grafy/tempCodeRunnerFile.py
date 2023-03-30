from collections import deque

def Bridge(G):
    n = len(G)
    P = [None for i in range(n)]
    visited = [False for i in range(n)]
    d = [ float('inf') for i in range(n) ]
    low = [ float('inf') for i in range(n) ]
    time = 0
    def DFSVisit( u ):
        nonlocal time, visited, d, G, low, P

        visited[u] = True
        d[ u ] = time
        low[ u ] = d[ u ]
        time += 1


        for v in G[u]:
            if not visited[v]:
                P[v] = u
                DFSVisit( v )
                low[ u ] = min( low[u], low[ v ] )
            elif v != P[ u ]:
                low[ u ] = min( low[u], low[ v ])
        
        if low[ u ] == d[ u ] and P[ u ] != None:
            print(u, P[u])

    for i in range(n):
        if not visited[i]:
            DFSVisit( i )


G = [ [1,6], [0,2], [1,3,6], [2,4], [3,5], [4,3], [0,2,7], [6]]
Bridge(G)