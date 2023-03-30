from random import randint

def CountSort(T,n,k):
    A=[0 for _ in range(n)]
    Sorted=[0 for _ in range(n)]
    for el in T:
        if k==1: index=el%n
        else: index=el//n
        A[index]+=1
    for i in range(1,n):
        A[i]+=A[i-1]
    for el in T:
        if k==1: index=el%n
        else: index=el//n
        Sorted[A[index]-1]=el
        A[index]-=1
    return Sorted
def Radix(T,n):
    T=CountSort(T,n,1)
    T=CountSort(T,n,0)
    return T

n=100
T=[randint(0,n*n-1) for _ in range(n)]
print(T)
T=Radix(T,n)
print(T)
