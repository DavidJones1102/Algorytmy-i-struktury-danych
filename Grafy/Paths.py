from queue import PriorityQueue

def Dijsktra( G, s, t):
    n = len( G )
    PQ = PriorityQueue()
    d = [ float("inf") for i in range(n) ]

    d[ s ] = 0
    PQ.put( (0,s) )

    while not PQ.empty():
        min_dist, min_v = PQ.get()

        for u,w in  G[ min_v ]:
            if d[ u ] > d[ min_v ] + w:
                d[ u ] = d[ min_v ] + w
                PQ.put( (d[u], u) )
    return d

def path( G ):
    n = len( G )
    ds = Dijsktra( G, s, t )
    dt = Dijsktra( G, t, s )
    dist = ds[t]
    ans = []
    for i in range( n ):
        for u,w in G[ i ]:
            if u > i and (ds[ u ] + w + dt[ i ] == dist or  ds[ i ] + w + dt[ u ] == dist):
                ans.append( (i,u) )
    print( ans )

 
G = [ [ (1,2), (2,4) ],
    [ (0,2), (3,11), (4,3) ],
    [ (0,4), (3,13) ],
    [ (1,11), (2, 13), (5,17), (6,1) ],
    [ (1,3), (5,5) ],
    [ (3,17), (4,5), (7,7) ],
    [ (3,1), (7,3) ],
    [ (5,7), (6,3)]
    ]
s = 0
t = 7

path(G)