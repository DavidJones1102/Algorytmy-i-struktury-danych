T = [[1,2,2,3],[4,1,3,4],[6,4,2,11]]
p =  5

def Plates(T,p):
    n = len(T)
    k = len(T[0])
    for i in range(n):
        for j in range(1,k):
            T[i][j]+=T[i][j-1]
    F = [[0 for i in range(n)] for t in range(p+1)]
    
    for t in range(1,k+1):
        if t<p:
            F[t][0] = T[0][t-1]
    #i stos 
    #t talerze
    for i in range(1,n):
        for t in range(1,p+1):
            if (i+1)*k>=t:
                max_val = F[t][i-1]
                for z in range(1,min(t+1,k+1)):
                    if F[t-z][i-1] != -1:
                        max_val = max(max_val, F[t-z][i-1]+T[i][z-1])
                F[t][i] = max_val
            else: F[t][i]=-1
    return F[p][n-1]
print(Plates(T,p))