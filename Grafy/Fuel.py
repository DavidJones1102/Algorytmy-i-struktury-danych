import queue

def Fuel( G, cost, start, end, tank ):
    n = len( G )
    parent = [ None for _ in range( n ) ]
    PQ = queue.PriorityQueue()

    d = [[ float('inf') for _ in range( tank+1 ) ] for i in range( n ) ]
    d[ start ][ 0 ] = 0

    PQ.put( ( 0, start, 0 ) )

    while not PQ.empty():
        c, v, t = PQ.get()
        for i in range( n ):
            if G[v][i] != 0:
                if t >= G[v][i] and d[i][t-G[v][i]] > c:
                    d[i][t-G[v][i]] = c
                    parent[ i ] = v
                    PQ.put( ( c, i, t-G[v][i] ) )
                    
                if t < tank and d[ v ][ t + 1 ] > d[ v ][ t ] + cost[v]:
                    d[ v ][ t + 1 ] = d[ v ][ t ] + cost[v]
                    PQ.put( ( d[ v ][ t + 1 ], v, t+1 ) )
    
    return d[ end ][ 0 ]


G = [ 
    [0, 1, 0, 0, 0, 4],
    [1, 0, 3, 0, 0, 0],
    [0, 3, 0, 1, 0, 0],
    [0, 0, 1, 0, 2, 3],
    [0, 0, 0, 2, 0, 0],
    [4, 0, 0, 3, 0, 0]
]
cost = [3, 8, 2, 6, 5, 4]
tank = 8
start = 0
end = 4

print( Fuel( G, cost, start, end, tank ) )
