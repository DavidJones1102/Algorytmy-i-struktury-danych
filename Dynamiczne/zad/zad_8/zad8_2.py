from zad8ktesty import runtests 
# F[a][b] = min(F[a-1][b],F[a-1][b-1],F[a][b-1])+1
#           ^if s[a]=!s[b]
#         = F[a-1][b-1] 
#         
def rek(F,s,t,a,b):
    if a==0 and b==0:
        if s[a]==t[b]: return 0
        else: return 1
    if F[a][b] != -1: return F[a][b]

    n = len(s) + len(t) 
    r1,r2,r3 = n,n,n
    if s[a]==t[b]:
        if a==0:
            F[a][b] = b
            return b
        if b==0:
            F[a][b] = a
            return a
        F[a][b] = rek(F,s,t,a-1,b-1)
        return F[a][b]
    elif a>0 and b>0:
        r1 = rek(F,s,t,a-1,b-1)
        r2 = rek(F,s,t,a-1,b)
        r3 = rek(F,s,t,a,b-1)
    elif b==0:
        r2 = rek(F,s,t,a-1,b)
    elif a==0: 
        r3 = rek(F,s,t,a,b-1)
    F[a][b] = min(r1,r2,r3)+1
    return F[a][b]


def napraw ( s, t ):
    ns = len(s)
    nt = len(t)

    F = [[-1 for i in range(nt)] for j in range(ns)]
    F[ns-1][nt-1] = rek(F,s,t,ns-1,nt-1)

    return F[ns-1][nt-1] 

runtests ( napraw )