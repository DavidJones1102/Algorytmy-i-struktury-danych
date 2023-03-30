def Parent( i ):
    return (i-1)//2
def Left( i ):
    return 2*i + 1
def Right( i ):
    return 2*i + 2
def FindSize( n ):
    size = 1
    while n > size:
        size *= 2
    return size
def Update( T, I, i ):
    T[I[i]] = (T[I[i]]+1)%3

    if T[I[i]] == 2:
        p = I[i]
        while p>0:
            p = Parent( p )
            T[p]+=1
    elif T[I[i]] == 0:
        p = I[i]
        while p>0:
            p = Parent( p )
            T[p]-=1


def Lamps( n, L ):
    size = FindSize( n )
    I = [ 2*size-1-i for i in range(size,0,-1) ]
    T = [ 0 for i in range( 2*size ) ]
    max_b = 0

    for a,b in L:
        for i in range(a,b+1):
            Update(T,I,i) 
        max_b = max(max_b,T[0])
    return max_b





class Node:

    def __init__(self):
        p = None
        l = None
        r = None

print( Lamps( 8, [(0,4),(2,7),(3,7)] ) ) 