from queue import PriorityQueue

def Dijkstra(G, P, d, a, b):
    n = len( G )
    parent = [ None for i in range( n ) ]
    distance = [ float('inf') for i in range( n ) ]
    PQ = PriorityQueue()

    distance[ a ] = 0
    PQ.put( (0,a) )

    while not PQ.empty():
        min_dist, min_v = PQ.get()

        for i in range( n ):
            if G[ min_v ][ i ] != -1 and G[ min_v ][ i ] <= d and \
                distance[ i ] > distance[ min_v ] + G[ min_v ][ i ]:

                distance[ i ] = distance[ min_v ] + G[ min_v ][ i ]
                parent[ i ] = min_v
                PQ.put( (distance[ i ],i) )
    
    if parent[ b ] is None:
        return None
    ans = []
    p = b
    while p is not None:
        ans.append( p )
        p = parent[ p ]
    return ans[::-1]

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]

print( Dijkstra(G,P,3,0,2))