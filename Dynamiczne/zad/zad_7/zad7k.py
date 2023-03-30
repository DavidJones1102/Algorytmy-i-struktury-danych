from zad7ktesty import runtests 
import collections

def ogrodnik (T, D, Z, l):
    m = len(T)
    n = len(T[0])
    drzewa = len(D)
    W = [0 for i in range(drzewa)]
    #BFS
    steps = [(-1,0),(1,0),(0,1),(0,-1)]
    for i in range(drzewa):
        d = D[i]
        Q = collections.deque()

        Q.append((0,d))
        W[i]+=T[0][d]
        T[0][d] = 0

        while len(Q) > 0:
            h,x = Q.pop()

            for dh,dx in steps:
                if 0<=h+dh<m and 0<=x+dx<n and T[h+dh][x+dx]!=0: 
                    W[i]+=T[h+dh][x+dx]
                    T[h+dh][x+dx]=0
                    Q.appendleft((h+dh,x+dx))


    F = [[0 for i in range(drzewa)] for w in range(l+1)]

    for w in range(W[0],l+1):
        F[w][0] = Z[0]
    
    for w in range(l+1):
        for i in range(1,drzewa):
            F[w][i] = F[w][i-1]
            if w>=W[i]:
                F[w][i] = max(F[w][i], F[w-W[i]][i-1] + Z[i])

    return F[l][drzewa-1]

runtests( ogrodnik, all_tests=True )
