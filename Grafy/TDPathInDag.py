

def BF( G, s ):
    n = len( G )
    G = [[ G[j][i] if j==i or G[j][i] != 0 else float('inf') for i in range( n )] for j in range( n )]
    E = []
    d = [ float('inf') for i in range(n) ]
    d[s] = 0
    for i in range( n ):
        for j in range( n ):
            if G[i][j]!=float('inf'):
                E.append( (i,j,G[i][j]) )
    
    for _ in range( n ):
        for u,v,w  in E:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
    
    for u,v,w  in E:
        if d[v] > d[u] + w:
            print( "Negative cycle ")
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
print(BF(G, 3))