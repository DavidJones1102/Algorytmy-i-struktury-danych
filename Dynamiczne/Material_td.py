# A = [xi,yi,ci]

A = [(1,3,5),(2,1,4),(5,3,8),(9,4,15)]
X = 10
Y = 10

# f(x,y) = max(f(xp,yp) + max(f(x-xp,y)+f(xp,y-yp), f(x-xp,y-yp)+f(x,y-yp)))
# for every p in A
def cut(A,X,Y):
    F = [[0 for y in range(Y+1)]for x in range(X+1)]
    n = len(A)
    for x in range(1,X+1):
        for y in range(1,Y+1):
            max_val = 0 
            for i in range(n):
                xp = A[i][0]
                yp = A[i][1]
                c = A[i][2]
                if xp <= x and yp <= y:
                    max_val = max(max_val,c+ max(F[x-xp][y]+F[xp][y-yp], F[x-xp][y-yp]+F[x][y-yp]))
            F[x][y] = max_val
    return F[X][Y]

print(cut(A,X,Y))