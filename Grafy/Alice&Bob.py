from queue import PriorityQueue

def Dijkstra(G, a, b):
    n = len( G )
    parent = [ [None,None] for i in range( n ) ]
    distance = [ [ float('inf'),float('inf') ] for i in range( n ) ]
    PQ = PriorityQueue()

    distance[ a ] = [0,0]
    # 1 Ania dojechała 0 Bob
    PQ.put( (0,a,1) )
    PQ.put( (0,a,0) )

    while not PQ.empty():
        min_dist, min_v, f = PQ.get()

        for i in range( n ):
            
            if G[ min_v ][ i ] != -1:
                if f==0 and distance[ i ][ 1 ] > distance[ min_v ][ 0 ] + G[ min_v ][ i ]:
                    distance[ i ][ 1 ] = distance[ min_v ][ 0 ] + G[ min_v ][ i ]  
                    parent[ i ][ 1 ] = min_v #f dojechało tutaj
                    PQ.put( (distance[ i ][ 1 ], i, 1 ) ) 
                elif f==1 and distance[ i ][ 0 ] > distance[ min_v ][ 1 ]:
                    distance[ i ][ 0 ] = distance[ min_v ][ 1 ]
                    parent[ i ][ 0 ] = min_v
                    PQ.put( (distance[ i ][ 0 ], i, 0 ) )

    print(min(distance[b]))
    ans = []
    if distance[ b ][ 1 ] < distance[ b ][ 0 ]:
        f = 1
        p = b
        while p is not None:
            ans.append( p )
            p = parent[p][f]
            if f==1: f=0
            else: f=1
    else:
        f = 0
        p = b
        while p is not None:
            ans.append( p )
            p = parent[p][f]
            if f==1: f=0
            else: f=1
            
    print(ans[::-1], f)
            
   

G = [
[-1, 6,-1, 3, 4],
[-1,-1, 7, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
G = [
[-1, 6,-1, 3, 4,-1],
[-1,-1, 7, 3,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1,-1],
[-1,-1, -1,-1,-1,2],
[-1,-1,2,-1,-1,-1]]

Dijkstra(G,0,2)