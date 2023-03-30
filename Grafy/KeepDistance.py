# Algorytm znajdowania ścieżki dla pojazdu A z x do y 
# i równolegle dla pojazdu B z y do x 
# tak aby dystans pomiędzy pojazdami podczas całej trasy zawsze był większy od d
# drogi są podane jako graf ważony w postaci macierzowej
from collections import deque

def KeepDist( M, x, y, d ):
    n = len( M )
    Min_distances_in_M = [[ float('inf') if j!=i and M[j][i] == 0 else M[j][i] for i in range( n ) ] for j in range( n )]
    
    # Floyd Warshal (najkrótsze sćieżki pomiedzy wierzchołkami grafu)
    for k in range( n ):
        for v in range( n ):
            for u in range( n ):
                Min_distances_in_M[v][u] = min( Min_distances_in_M[v][u], Min_distances_in_M[v][k] + Min_distances_in_M[k][u])
    
    # G - zmodyfikowany graf, zawiera pary (v,u) możliwych pozycji samochodu A i B 
    # ale tylko takie których odległość jest większa od d 
    G = [ [ [] if Min_distances_in_M[j][i] >= d else -1 for i in range( n ) ] for j in range( n ) ]
    for v1 in range( n ):
        for u1 in range( n ):
            if G[v1][u1] != -1 and G[v1][u1] != 0:
                for v2 in range( n ):
                    for u2 in range( n ):   
                        if G[v2][u2] != -1 and G[v1][u1] != 0 and M[v1][v2] != 0 and M[u1][u2] != 0 and (v1!=v2 or u1!=u2):
                            G[v1][u1].append( (v2,u2) )
    
    # na zmodyfikowanym grafie puszczamy BFS
    visited = [ [False for i in range( n )] for j in range( n )]
    parent = [ [ (-1,-1) for i in range( n )] for j in range( n )]
    Q = deque()
    Q.append( (x,y) )
    visited[x][y] = True

    while len(Q):
        v1,u1 = Q.pop()
        for v2,u2 in G[v1][u1]:
            if not visited[v2][u2]:
                visited[v2][u2] = True
                parent[v2][u2] = (v1,u1)
                Q.append( (v2,u2) )
    
    pv,pu = y,x
    ans = []
    while pv != -1:
        ans.append( (pv,pu) )
        pv,pu = parent[pv][pu]

    
    return ans[::-1]
                            

M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2

M = [
[0,1,0,3,0,0],
[1,0,2,0,0,0],
[0,2,0,1,1,2],
[3,0,1,0,0,0],
[0,0,1,0,0,3],
[0,0,2,0,3,0]
]
x=0
y=4
d=3
print(KeepDist(M,x,y,d))