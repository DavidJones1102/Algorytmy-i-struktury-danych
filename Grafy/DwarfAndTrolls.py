from collections import deque
# s place where are dwarfs
# w[ v ] - amount of trolls on v 
def Bridge(G, w, s):
    n = len(G)
    P = [None for i in range(n)]
    visited = [False for i in range(n)]
    d = [ float('inf') for i in range(n) ]
    low = [ float('inf') for i in range(n) ]
    time = 0
    amount = [ 0 for i in range(n) ]
    
    def DFSVisit( u ):
        nonlocal time, amount, w, visited, d, G, low, P

        visited[u] = True
        d[ u ] = time
        low[ u ] = d[ u ]
        time += 1
        trolls = w[u]

        for v in G[u]:
            if not visited[v]:
                P[v] = u
                trolls+=DFSVisit( v )
                low[ u ] = min( low[u], low[ v ] )
            elif v != P[ u ]:
                low[ u ] = min( low[u], low[ v ])
        
        amount[u] = trolls
        
        if low[ u ] == d[ u ] and P[ u ] != None:
            print(u, P[u], amount[u] )
        return trolls
    DFSVisit( s )


G = [ [1,6], [0,2], [1,3,6], [2,4], [3,5], [4,3,8], [0,2,7], [6], [5]]
w = [ 5, 4, 0, 4, 5, 3, 2, 5, 100]
s = 2
Bridge(G, w, s)