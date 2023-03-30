T = [1,-5,2]
#F[i,j] = min(max(F[i,k],F[k+1,j],F[k+1,j]+F[i,k]))
def rek(T,F,i,j):
    if i==j:
        F[i][i] = (abs(T[i]),T[i])
        return F[i][i]
    if i==j-1:
        F[i][j] = (abs(T[i]+T[j]),T[i]+T[j])
        return F[i][j]
    if F[i][j] != None: return F[i][j]
    min_val = 420

    for k in range(i,j):
        r1 = rek(T,F,i,k)
        r2 = rek(T,F,k+1,j)
        if min_val>max(r1[0],r2[0],abs(r1[1]+r2[1])): 
            min_s = r1[1]+r2[1]
            min_val = max(r1[0],r2[0],abs(r1[1]+r2[1]))
    F[i][j] = (min_val,min_s)
    return F[i][j]

def OptimalSum(T):
    n = len(T)

    F = [[None for i in range(n)] for j in range(n)]
    F[0][n-1] = rek(T,F,0,n-1)

    return F[0][n-1][0]
print(OptimalSum(T))