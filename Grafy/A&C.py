def Extend( G ):
    pass
def MaxFlow( K, A ):
    n = len(K)
    m = len(A)

    G = [[ 0 for i in range( n+m+2 )] for j in range( n+m+2 )]
    for i in range( n ):
        for app in K[i]:
            G[app+1][m+i+1] = 1
    for i in range( m ):
        G[0][i+1] = A[i]
    for i in range( n ):
        G[ m+i+1 ][ m+n+1 ] = 1
    return G
A = [ 1, 0, 2, 1 ]
K = [ [0,1,2,3], [2], [1,2], [2, 3] ]

MaxFlow( K, A )