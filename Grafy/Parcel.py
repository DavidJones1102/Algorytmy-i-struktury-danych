from collections import deque

def Parcel(G,K):
    n = len( G )
    # Znajdowanie skrajnie "prawego" domu do którego mamy dostarczyć paczke
    d = [ None for i in range(n) ]
    visited = [ False for i in range(n) ]
    Q = deque()
    Q.append(0)
    d[ 0 ] = 0
    visited[ 0 ] = True
    while len(Q):
        v = Q.pop()
        for u in G[ v ]:
            if not visited[u]:
                visited[ u ] = True
                d[ u ] = d[ v ] + 1
                Q.appendleft( u )

    extreme_left = K[0]
    for i in K:
        if d[ extreme_left ] < d[ i ]:
            extreme_left = i

    #znajdowanie skrajnie "lewego" domu do którego mamy dostarczyć paczkę
    d = [ None for i in range(n) ]
    parent = [ None for i in range(n) ]
    visited = [ False for i in range(n) ]
    Q = deque()
    Q.append( extreme_left )
    d[ extreme_left ] = 0
    visited[ extreme_left ] = True
    while len(Q):
        v = Q.pop()
        for u in G[ v ]:
            if not visited[u]:
                visited[ u ] = True
                parent[ u ] = v
                d[ u ] = d[ v ] + 1
                Q.appendleft( u )
    extreme_right = K[0]
    for i in K:
        if d[ extreme_right ] < d[ i ]:
            extreme_right = i

    #znajdujemy wierzchołki należące do średnicy
    diameter = []
    p = extreme_right
    while p != extreme_left:
        diameter.append( p )
        p = parent[ p ]
    diameter.append( extreme_left )

    # odległość to długość średnicy +(2 * odległość domów nie na średnicy od średnicy)
    dist = d[ extreme_right ]
    for el in K:
        p = el
        while p not in diameter:
            dist+=2
            p = parent[ p ]
    
    return dist

    
G = [ [1], [0,2], [1,3,4,6], [2,10,11], [2,5], [4], [2,7,9], [6,8], [7], [6], [3], [3] ]
K = [1,2,5,7,9]

Parcel( G, K )

     