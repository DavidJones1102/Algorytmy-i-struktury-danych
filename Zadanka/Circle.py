from cmath import sqrt

def partition(A,start,end):

    pivot=A[end]
    b=start-1
    for i in range(start,end+1):
        if A[i]<=pivot:
            b+=1
            A[i],A[b]=A[b],A[i]
    return b

def QuickSort(A,start,end):
    while start<end:
        q=partition(A,start,end)

        if q-1-start<end-q+1:
            QuickSort(A,start,q-1)
            start=q+1
        else:
            QuickSort(A,q+1,end)
            end=q-1
A=[1,4,2,6,2,7,3]
QuickSort(A,0,len(A)-1)
print(A)
def index(p,k):
    r=sqrt(p[0]**2+p[1]**2)

    return
def Circle(A,k):
    n=len(A)
    Buckets = [[] for _ in range(n)]

    for el in A:
        Buckets[index(el,k)].append(el)
    
    for B in Buckets:
        QuickSort(B,0,len(B)-1)

    k=0
    for i in range(n):
        for j in range(len(Buckets[i])):
            A[k]=Buckets[i][j]
            k+=1
    


