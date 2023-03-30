# M - nominały
# C - cena
# M = [2, 5, 8, 11]
# C = 9 
# ans True
# f(i,c) - czy możliwe jest zapłacenie kwoty c
# monetami o nominałach M[0,...,i]

def f(M,C):
    n = len(M)
    F = [[False for c in range(C+1)] for i in range(n)]

    for i in range(n): F[i][0] = True
    for c in range(0,C+1,M[0]): F[0][c] = True

    for i in range(1,n):
        for c in range(1,C+1):
            F[i][c] = F[i-1][c]
            if c >= M[i]:
                F[i][c] |= F[i-1][c-M[i]]

    return F[n-1][C]
M = [3, 5, 8, 11]
C = 14

print(f(M, C))