from zad3testy import runtests

def cut(a1,b1,a2,b2): 
    if a2 >= b1 or a1 >= b2: 
        return (0,0)

    elif a1<=a2<=b1<=b2: # 
        return (a2,b1)

    elif a1<=a2<=b2<=b1:
        return (a2,b2)

    elif a2<=a1<=b2<=b1:
        return (a1,b2)

    elif a2<=a1<=b1<=b2:
        return (a1,b1)

        
def kintersect( A, k ):
    n = len( A )
    DP = [ [ (0,0) for i in range(k+1)] for j in range(n) ]

    
    DP[0][1] = ( A[0][0], A[0][1] )
    for i in range( n ):
        DP[i][0] = ( 0, float('inf') )

    for i in range( 1,n ):
        for p in range( 1,k+1 ):
            cut1 = DP[i-1][p][1] - DP[i-1][p][0]
            x = cut(DP[i-1][p-1][0],DP[i-1][p-1][1],A[i][0],A[i][1])
            cut2 = x[1]-x[0]

            if cut1 >= cut2:
                DP[i][p] = DP[i-1][p]
            else:
                DP[i][p] = x
    
    ans = []
    wynik = DP[n-1][k]
    for j in range( n ):
        if wynik[0]>=A[j][0] and wynik[1] <= A[j][1]:
            ans.append(j)

    return ans


print(cut(100,100,60,120))
runtests( kintersect )
