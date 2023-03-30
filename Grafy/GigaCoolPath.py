import queue

def dijkstra( G, s, t ):
    PQ = queue.PriorityQueue()
    n = len( G )
    parent = [ None for i in range(n) ]
    d = [ (float('inf'), float('inf')) for i in range(n) ]

    PQ.put( ( 0, s ) )
    d[ s ] = ( 0, 0 )

    while not PQ.empty():
        _, v = PQ.get()
        v_w, v_l = d[ v ]

        for i in range( n ):
            w = G[v][i]
            path_w, path_l = d[ i ]
            if  w != 0 and path_w > v_w + w:
                d[ i ] = ( v_w + w, v_l + 1)
                parent[ i ] = v
                PQ.put( (v_w + w, i) )
            elif w != 0 and path_w == v_w + w and v_l + 1 < path_l:
                d[ i ] = ( v_w + w, v_l + 1)
                parent[ i ] = v
                PQ.put( (v_w + w, i) )

    path = [ t ]

    while parent[ t ] != None:
        path.append( parent[ t ] )
        t = parent[ t ]

    return path[::-1]

G = [
    [0, 2, 0, 0, 1],
    [2, 0, 1, 0, 1],
    [0, 1, 0, 1, 2],
    [0, 0, 1, 0, 1],
    [1, 1, 2, 1, 0]
]
s = 0
t = 2
print( dijkstra(G, s, t ))