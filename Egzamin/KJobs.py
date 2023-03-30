def KJobs( J, k ):
    n = len(J)
    D = [[ float('inf') if j+1>=i else None for i in range( k+1 )] for j in range( n ) ]
    for s in range( n ):
        if D[s][0] != None:
            D[s][0] = 0
        if D[s][1] != None:
            D[s][1] = 0
        
    for i in range( n ):
        for x in range( 2, k+1 ):
            for j in range( x-1, i ):
                if J[i][0]>=J[j][1]:
                    D[i][x] = min( D[i][x], D[j][x-1] + J[i][0]-J[j][1])
    
    ans = float('inf')
    for i in range( k, n ):
        ans = min(ans, D[i][k])

    return ans


J = [ (1,3),(2,5),(5,9) ]
k = 2

KJobs(J,k)