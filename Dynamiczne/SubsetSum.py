#Napisać print wyniku!
#A = [1,7,2,8,3,5]
#T = 6
#Does subset of A, 
#which sum is eq T exist?
#  Suma
# I
# n
# d
# e
# x
#                       t>=A[i]
# f(i,t)={f(i-1,t) or f(i-1,t-A[i])}
#
#F[index, suma]

def SubsetSum(A,T):
    n = len(A)
    F = [[False for _ in range(T+1)] for i in range(n)]
    for i in range(n):
        F[i][0] = True
    if A[0] <= T:
        F[0][A[0]] = True
    
    for i in range(1,n):
        for t in range(T+1):
            F[i][t] = F[i-1][t]
            if A[i] <= t:
                F[i][t] |= F[i-1][t-A[i]]

    return F[n-1][T]

A = [8,3,7,8,3,5]
T = 6

print(SubsetSum(A,T))

