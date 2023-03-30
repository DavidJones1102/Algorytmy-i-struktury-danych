from math import log10
# Ścieżka o najmniejszym iloczynie 

def BestExchange( G, A, B):
    n = len( G )
    G = [[ log10(G[i][j]) if G[i][j]!=0 else float('inf') for j in range( n )] for i in range( n )]
    parent = [-1 for _ in range( n )]
    d = [ float('inf') for _ in range( n )]
    d[ A ] = 0
    edge = []
    for u in range( n ):
        for v in range( n ):
            if G[u][v] != float('inf'):
                edge.append( (u,v,G[u][v]) )
    
    for _ in range( n ):
        for e in edge:
            u,v,w = e
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parent[v] = u
    
    for e in edge:
        u,v,w = e
        if d[v]>d[u] + w:
            return None
    ans = []
    while B != -1:
        ans.append(B)
        B=parent[B]

    return ans[::-1]             
                 
G = [
    [0,3,4,5],
    [3,0,1/2,1],
    [4,2,0,4],
    [5,1,4,0]
    ]
    

print( BestExchange(G,0,2) )