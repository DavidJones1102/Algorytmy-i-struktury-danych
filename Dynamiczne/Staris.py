A = [1,4,2,4,5,1,2,3]

def stairs(A):
    n = len(A)
    F = [0 for i in range(n)]
    F[0] = 1

    for i in range(n):
        for k in range(i+1,i+A[i]+1):
            if k<n:
                F[k]+=F[i]
    return F[n-1]
print(stairs(A))
