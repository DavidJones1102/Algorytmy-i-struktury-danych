from zad11ktesty import runtests
def rek(F,T,S,i,p):
    if i==len(T)-1:
        return abs(S-p - p)
    
    if F[p][i] != None: return F[p][i]

    w2 = rek(F,T,S,i+1,p+T[i])
    w1 = rek(F,T,S,i+1,p)
    
    F[p][i] = min(w1,w2)

    return F[p][i]


def kontenerowiec(T):
    n = len(T)
    S = 0
    for i in range(n):
        S+=T[i]

    F = [[None for i in range(n)] for i in range(S+1)]
    F[0][0] = rek(F,T,S,0,0)

    return F[0][0]

runtests ( kontenerowiec )
    