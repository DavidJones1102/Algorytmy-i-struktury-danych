from zad9ktesty import runtests
from math import inf
def rek(P,F,l1,l2,i):
    if i==len(P)-1:
        return 0
        
    if F[i][l1][l2] != -1:
        return F[i][l1][l2]

    if P[i] > l1 and P[i] > l2:
        F[i][l1][l2] = 0
        return 0
        
    if P[i] > l2:
        F[i][l1][l2] = rek(P,F,l1-P[i],l2,i+1)+1
    elif P[i] > l1:
        F[i][l1][l2] = rek(P,F,l1,l2-P[i],i+1)+1
    else:
        w1 = rek(P,F,l1-P[i],l2,i+1)+1
        w2 = rek(P,F,l1,l2-P[i],i+1)+1
        F[i][l1][l2] = max(w1,w2)

    return F[i][l1][l2]


def prom(P, g, d):
    n = len(P)
    F = [[[-1 for i in range(g+1)] for j in range(d+1)] for k in range(n)]
    F[0][d][g] = rek(P,F,d,g,0)

    l1 = d
    l2 = g
    i = 0

    sol1 = []
    sol2 = []

    while i<n and (l1>=P[i] or l2 >=P[i]):

        if l1 < P[i]:
            w1 = 0
            w2 = 1
        elif l2 < P[i]:
            w1 = 1
            w2 = 0
        else:
            w1 = rek(P,F,l1-P[i],l2,i+1)
            w2 = rek(P,F,l1,l2-P[i],i+1)
        
        if w1 > w2:
            sol1.append(i)
            l1-=P[i]
        else:
            sol2.append(i)
            l2-=P[i]
        i+=1
    
    if i-1 in sol1:
        return sol1
    else: return sol2


runtests ( prom )