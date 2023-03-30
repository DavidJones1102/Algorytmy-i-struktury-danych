from zad1testy import runtests
from collections import deque

def intuse( I, x, y ):
    n = len( I )
    G = [ [] for i in range( n ) ]
    R = [ [] for i in range( n ) ]
    S = []
    E = []

    for i in range( n ):
        if I[i][0]==x:
            S.append(i)
        elif I[i][1] ==y:
            E.append(i)
        for j in range( n ):
            if I[i][1] == I[j][0] and i!=j:
                G[i].append(j)
                R[j].append(i)
    visited1 = [False for i in range(n) ]
    Q = deque(S)
    for el in S:
        visited1[el] = True

    while len(Q):
        v = Q.pop()
        for u in G[v]:
            if not visited1[ u ]:
                visited1[ u ]=True
                Q.appendleft( u )
    visited2 = [False for i in range(n) ]
    Q = deque(E)
    for el in E:
        visited2[el] = True

    while len(Q):
        v = Q.pop()
        for u in R[v]:
            if not visited2[ u ]:
                visited2[ u ]=True
                Q.appendleft( u )
    
    ans = []

    for i in range( n ):
        if visited1[i] and visited2[i]:
            ans.append(i)
    return ans


runtests( intuse )
