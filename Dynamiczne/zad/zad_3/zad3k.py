from zad3ktesty import runtests

def ksuma( T, k ):
    n = len(T)
    f = [0 for i in range(n)]
    for j in range(min(k,n)):
        f[j]=T[j]

    for i in range(k,n):
        min_val = T[i]+f[i-1]
        for j in range(2,min(i,k)+1):
            min_val = (min(min_val, T[i] + f[i-j]))
        f[i] = min_val

    min_val = f[n-1]
    for j in range(1,min(k,n)+1):
        min_val = min(min_val, f[n-j])

    return min_val
    
runtests ( ksuma )