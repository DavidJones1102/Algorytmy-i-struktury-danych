#A = [1,7,2,3,4]
#B = [2,5,1,4]
#ans 2 (2,4)
#f(i,j) - lcs from A[0,...,i] and B[0,...,j]
#f(i,j) = max{f(i-1,j), f(i,j-1), }
def LCS(A ,B):
    n1 = len(A)
    n2 = len(B)

    F = [[0 for _ in range(n1)] for i in range(n2)]
    for i in range(n1):
        if A[i] == B[0]:
            F[0][i] = 1
    for j in range(n2):
        if B[j] == A[0]:
            F[j][0] = 1
            
    for j in range(1,n1):
        for i in range(1,n2):
            F[i][j] = max(F[i-1][j], F[i][j-1])
            if A[j] == B[i]:
                F[i][j] = max(F[i][j], F[i-1][j-1] + 1)
    return F[n2-1][n1-1]

A = [1,7,2,3,4]
B = [2,5,1,4]
print(LCS(A,B))