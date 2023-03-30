#A=[2,5,3,5,6,2,6,8,4,7,3]
#F[i] - najdłuższy rosnący podciąg w A[0]...A[i]
#F=[1,2,2,3,4,1,4,5,3,5,2]
#P[i] - indexs poprzedniego elementu w rosnącym podciągu
#P=[-1,0,0,2,3,-1,3,4,2,4,0]
def print_sol(A,P,i): 
    if P[i] != -1:
        print_sol(A,P,P[i])

    print(A[i], end=" ")


def LCS(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[i] > A[j] and F[i] < F[j]+1:
                F[i] = F[j]+1
                P[i] = j
 
    max_i = 0
    for i in range(n):
        if F[max_i] < F[i]:
            max_i=i
   
    print_sol(A,P,max_i)



#A=[2,5,3,5,6,2,6,8,4,7,3]
#LCS(A)