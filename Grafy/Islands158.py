from queue import PriorityQueue

def Islands( G, A, B ):
    n = len( G )
    d = [ float('inf') for _ in range(n) ]
    PQ = PriorityQueue()
    
    d[ A ] = 0
    # wkładamy do kolejki ( cene, wierzchołek, czym do niego dotarliśmy )   
    PQ.put( ( d[ A ], A, -1 ) )   

    while not PQ.empty():
        dist, v, prev = PQ.get()

        for u in range( n ):
            if G[u][v] != 0 and d[ u ] and G[u][v] != prev and d[ u ] > dist + G[ u ][ v ]:
                d[ u ] = dist + G[ u ][ v ]
                PQ.put( (d[ u ], u, G[ u ][ v ]) )
    
    return d[ B ]


G = [
    [0,5,1,8,0,0,0],
    [5,0,0,1,0,8,0],
    [1,0,0,8,0,0,8],
    [8,1,8,0,5,0,1],
    [0,0,0,5,0,1,0],
    [0,8,0,0,1,0,5],
    [0,0,8,1,0,5,0]
]
A = 5
B = 2
# ans = 13
print( Islands(G,A,B) )