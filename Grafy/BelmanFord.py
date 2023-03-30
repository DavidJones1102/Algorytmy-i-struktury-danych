def BellmanFord(G, s):
    n = len(G)
    G = [ [ float('inf') if G[i][j]==0 else G[i][j] for i in range(n)] for j in range(n)]
    
    d = [ float('inf') for i in range(n) ]
    d[ s ] = 0
    edge = []
    for u in range( n ):
        for v in range( n ):
            if G[u][v] != float('inf'):
                edge.append((u,v,G[u][v]))

    for _ in range( n ):
        for e in edge:
            v,u,w = e
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                
    for e in edge:
        v,u,w = e
        if d[v] > d[u] + w:
            print("Negative cycle")
            return None
    return d

G = [   [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
print(BellmanFord(G, 3))