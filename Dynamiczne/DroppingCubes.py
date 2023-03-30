A = [(1,4),(0,5),(1,5),(2,6),(2,4)] 
# ans: 3
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]
# ans: 2
# f(i) - the highest pyramid based on cube ai
# f(n-1) = 1 
# f(i) = max(f(i+k))
# k from 1 to n-1-i

def cubes(A):
    n = len(A)
    F = [1 for i in range(n)]
    Upper = [-1 for i in range(n)]
    
    for i in range(n-1,-1,-1):
        for k in range(i+1,n):
            if F[k]+1>F[i] and A[k][0]>=A[i][0] and A[k][1]<=A[i][1]:
                F[i] = F[k]+1
                Upper[i] = k
    max_i = 0
    max_v = F[0]
    for i in range(1,n):
        if max_v<F[i]:
            max_v = F[i]
            max_i = i
    
    while max_i!=-1:
        print(max_i,end=" ")
        max_i = Upper[max_i]
    return max(F)
print("\n",cubes(A))