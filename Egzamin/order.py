from collections import deque

def check( L, I, n, M ):
    Visited = [ False for i in range(n) ]
    ans = []
    def DFSVisit( a,b ):
        nonlocal Visited, L, I, n, M, ans
        index = I[a][b]
        Visited[index] = True
        for j in range( M ):
            if I[b][j] != -1 and not Visited[I[b][j]]:
                DFSVisit( b,j )
        ans.insert(0,L[I[a][b]][2])

    for i in range( n ):
        a,b,v = L[i]
        index = I[a][b]
        if index != -1 and not Visited[index]:
            DFSVisit(a,b)
    

    return ans

def order( L, K ):
    M = 10**K
    n = len( L )
    L = [ ( L[i]//(M),L[i]%(M),L[i]) for i in range( n )]
    I = [[ -1 for i in range(M)] for j in range(M) ] 

    for i in range( n ):
        a,b,v = L[i]
        I[a][b] = i
    
    ans = check(L,I,n,M)   

    return ans

def order( L, K ):
    M = 10**K
    n = len( L )
    L = [ ( L[i]//(M),L[i]%(M),L[i]) for i in range( n )]
    I = [[ -1 for i in range(M)] for j in range(M) ] 

    for i in range( n ):
        a,b,v = L[i]
        I[a][b] = i
    
    ans = check(L,I,n,M)   

    return ans


L = [56,15,31,43,54,35,12,23]
K = 1
print ( order(L,K) )

