from zad8ktesty import runtests 
# F[a][b] = min(F[a-1][b],F[a-1][b-1],F[a][b-1])+1
#           ^if s[a]=!s[b]
#         = F[a-1][b-1] 
#         
def napraw ( s, t ):
    ns = len(s)
    nt = len(t)

    F = [[-1 for i in range(nt)] for j in range(ns)]
    if s[0] == t[0]:
        F[0][0] = 0
    else: F[0][0] = 1
    f = True
    g = True
    for i in range(1,ns):
        if s[i]==t[0] and f:
            f=False
            F[i][0] = F[i-1][0]
        else: F[i][0] = F[i-1][0] + 1
    for j in range(1,nt):
        if t[j]==s[0] and g:
            g=False
            F[0][j] = F[0][j-1]
        else: F[0][j] = F[0][j-1] + 1

    for i in range(1,ns):
        for j in range(1,nt):
            if s[i]==t[j]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j],F[i-1][j-1],F[i][j-1]) + 1
        

    return F[ns-1][nt-1] 

runtests ( napraw )