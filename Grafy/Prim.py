from queue import PriorityQueue

def Prim(G):
    PQ = PriorityQueue()
    n = len(G)
    d = [ float('inf') for i in range(n) ]
    parent = [ None for i in range(n) ]
    d[0] = 0
    MST= []
    
    PQ.put( (0,0) )

    while not PQ.empty():
        w, t = PQ.get()
        for u,wu in G[t]:
            if d[u] > wu and parent[t] != u:
                d[u] = wu
                parent[u] = t
                PQ.put( (wu,u) )
                
    return parent


#def Prim(G):
#    PQ = PriorityQueue()
#    n = len(G)
#    visited = [ False for i in range(n) ]
#    visited[0] = True
#    MST= []
#    for u in G[0]:
#        PQ.put((u[1],0,u[0]))
#
#    while not PQ.empty():
#        w, v, t = PQ.get()
#        if not visited[t]:
#            visited[ t ] = True
#            MST.append((w, v, t))
#            for u in G[t]:
#                if not visited[u[0]]:
#                    PQ.put((u[1], t, u[0]))
#                
#    return MST
#G = [ [[16, 0, 1], [15, 0, 2],[ 37, 0, 3], [8, 1, 2], [22, 1, 3], [23, 2, 3]] ]
G = [ [(1,16),(2,15),(3,37)], [(0,16),(2,17),(3,22)],[(0,15),(1,17),(3,23)],[(0,37),(1,22),(2,23)]]

print(Prim(G))