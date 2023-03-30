def rek(F,s,i,j):
    if i==j:
        F[i][i] = s[i]
        return F[i][i]
    elif i==j-1:
        if s[i] == s[j]:
            F[i][j] = s[i:j+1]
            return F[i][j]
    if F[i][j] != -1: return F[i][j]
    r1 = rek(F,s,i+1,j)
    r2 = rek(F,s,i,j-1)
    
    if s[i]==s[j]:
        r3 = rek(F,s,i+1,j-1)
        r3 = s[i] + r3 + s[j]
        F[i][j] = r3
        return F[i][j]
    if len(r1)>len(r2):
        F[i][j] = r1
    else:
        F[i][j] = r2
    

    return F[i][j]
def Palindrom(s):
    n = len(s)
    F = [[ -1 for i in range(n)] for j in range(n)]

    F[0][n-1] = rek(F,s,0,n-1)

    return F[0][n-1]

print(Palindrom('character'))

    
        
