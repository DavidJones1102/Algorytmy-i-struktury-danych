S = ['ab','aba','ba','ba','b']
t = 'ababbab'
#abab|bab 3 - wynik algorytmu 
#ab|ab|ba|b 1

def solve(S,t):
    nt = len(t)
    F = [ -1 for i in range(nt+1)]
    P = [ -1 for i in range(nt+1)]
    if t[nt-1] in S:
        F[nt-1] = 1
        P[nt-1] = t[nt-1]
    F[nt] = nt+1
    for i in range(nt-2,-1,-1):
        min_val = -1 
        for s in S:
            n = len(s)
            if i+n<=nt and s==t[i:i+n] and F[i+n]!=-1:
                if min_val!=-1 and min(n, F[i+n])>min_val:
                    min_val =  min(n, F[i+n])
                    P[i] = s
                elif min_val==-1:
                    min_val = min(F[i+n],n)
                    P[i] = s
        F[i] = min_val
    
    while i<nt:
        for s in S:
            n = len(s)
            if i+n<=nt and s==t[i:i+n] and F[i+n]>=F[0]:
                print(s)
                i=i+n

    i=0
    print(P[i])
    i=i+len(P[i])
    while i<nt:
        print(P[i])    
        i=i+len(P[i])   


    return F[0]
print(solve(S,t))