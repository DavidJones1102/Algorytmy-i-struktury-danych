from zad5ktesty import runtests

def rek(A,DP,i,j):
    if i==j:
        DP[i][j] = (A[i],0)
        return DP[i][j]
    if i==j-1:
        DP[i][j] = (max(A[i],A[j]),min(A[i],A[j]))
        return DP[i][j]
    if DP[i][j]!=None:
        return DP[i][j]
    r1 = rek(A,DP,i+1,j)
    r2 = rek(A,DP,i,j-1)
    if A[i] + r1[1] > A[j] + r2[1]:
        DP[i][j] = (A[i] + r1[1],r1[0])
    else:
        DP[i][j] = (A[j] + r2[1],r2[0])
    return DP[i][j]

 
def garek ( A ):
    n = len(A)
    DP = [[None for i in range(n)] for j in range(n)]
    DP[0][n-1] = rek(A,DP,0,n-1)

    return DP[0][n-1][0]

runtests ( garek )