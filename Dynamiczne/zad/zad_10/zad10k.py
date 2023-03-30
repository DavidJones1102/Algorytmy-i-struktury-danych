from zad10ktesty import runtests

def dywany ( N ):
    F = [N for i in range(N+1)]
    F[0]=0
    k = 1
    while k*k<N+1:
        F[k*k] = 1
        k+=1
        if k*k==N: return [k]

    for i in range(1,N+1):
        if F[i] != 1:
            a=1
            while a*a < i:
                F[i] = min(F[i],F[i-a*a]+1)
                a+=1
    sol = []
    i=N
    while i!= 0:
        x=0
        while F[i] != F[i-x*x]+1:
            x+=1
        i=i-x*x
        sol.append(x)
        x=0
    return sol


runtests( dywany )

