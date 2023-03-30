#W - weights
#P - prices
#C - max capacity
#find max value
#
#f(i,c)=max(f(i-1,c),f(i-1,c-W[i])) 

def knapsack(W,P,C):
    n = len(W)
    F = [[0 for c in range(C+1)] for i in range(n)]

    for c in range(W[0],C+1):
        F[0][c] = P[0]

    for i in range(1,n):
        for c in range(C+1):
            F[i][c] = F[i-1][c]
            if c-W[i] >= 0:
                F[i][c] = max(F[i-1][c-W[i]]+P[i],F[i][c])
    return F[n-1][C]


W=[1,2,3,4,5]
P=[3,4,1,4,4]
C=7
print(knapsack(W,P,C))
