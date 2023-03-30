from zad12ktesty import runtests 
# F[j][k] = min( max(F[i][k-1], s[i][j]))
#           0<=i<j
def autostrada( T, k ):
    n = len(T)
    DP = [[None for i in range(k+1)] for j in range(n)]
    S = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        s = 0
        for j in range(i,n):
            s+=T[j]
            S[i][j] = s
    
    for i in range(n):
        DP[i][1] = S[0][i]

    for f in range(1,k+1):
        DP[0][f] = T[0]

    for j in range(1,n):
        for f in range(2,k+1):
            min_val = S[0][j]
            for i in range(j):
                min_val = min(min_val, max(DP[i][f-1], S[i+1][j]))
            DP[j][f] = min_val
    
    return DP[n-1][k]

runtests ( autostrada,all_tests=True )