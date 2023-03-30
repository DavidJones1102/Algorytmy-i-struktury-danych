
def GT(A):

    n=len(A)
    F = [0 for i in range(n)]
    P = [[] for i in range(n)]
    F[0] = A[0]
    P[0] = [0]
    F[1] = max(A[0],A[1])
    if A[0]>=A[1]:
        P[1] = [0]
    else: P[1] = [1]

    for i in range(2,n):
        
        if F[i-1] > F[i-2] + A[i]:
            F[i] = F[i-1]
            P[i] = P[i-1].copy()
        else:
            F[i] = F[i-2] + A[i]
            P[i] = i-2
            P[i] = P[i-2].copy()
            P[i].append(i)
    return P[n-1]
A = [1,5,1,1,5,4,3,1]
print(GT(A))