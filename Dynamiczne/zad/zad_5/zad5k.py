from zad5ktesty import runtests

def rek(A,DP,i,j):
    if i==j-1:
        DP[i][j]=max(A[i],A[j])
        return DP[i][j]
    if DP[i][j]!=-1:
        return DP[i][j]
    DP[i][j] = max(A[i] + min(rek(A,DP,i+2,j),rek(A,DP,i+1,j-1)), A[j] + min(rek(A,DP,i+1,j-1),rek(A,DP,i,j-2)))
    return DP[i][j]
def garek ( A ):
    n = len(A)
    DP = [[-1 for i in range(n)] for j in range(n)]
    DP[0][n-1] = rek(A,DP,0,n-1)
    return DP[0][n-1]

runtests ( garek )