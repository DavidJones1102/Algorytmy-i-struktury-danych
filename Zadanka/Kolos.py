def Prettiness(n):
    single=0
    multi=0
    t=[0 for _ in range(10)]
    while n>0:
        t[n%10]+=1
        n//=10
    for i in range(10):
        if t[i]==1: single+=1
        elif t[i]>1: multi+=1
    
    return single,multi
def Change(T):
    for i in range(len(T)):
        a,b=Prettiness(T[i])
        T[i]=T[i],a,b
     
def CountingSort(T,k): 
    n=len(T)
    A=[0 for _ in range(10)]
    Sorted=[0 for _ in range(n)]
    for i in range(n):
        index=T[i][k]
        A[index]+=1
    for i in range(1,n):
        A[i]+=A[i-1]
    for i in range(n-1,-1,-1):
        index=A[T[i][k]]
        A[T[i][k]]-=1
        Sorted[index-1]=T[i]
    return Sorted
def RadixSort(T):

    Change(T)
    T=CountingSort(T,2)
    T=T[::-1]
    T=CountingSort(T,1)
    for i in range(len(T)):
        T[i]=T[i][0]
    print(T)
 
#T=[1,5234,12344,1324123,123,123,43,123,44]
#RadixSort(T)
#1,1,1,4,4,2